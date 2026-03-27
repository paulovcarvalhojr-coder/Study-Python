# ── Imports ─────────────────────────────────────────────────────────────────

import hashlib          # módulo nativo para funções de hash criptográfico
from datetime import date  # tipo date para representar data de nascimento


# ── Validador de CPF (substitui banco.utils.validadores) ────────────────────

def validar_cpf(cpf: str) -> bool:
    """
    Valida CPF usando o algoritmo oficial dos dois dígitos verificadores.
    Recebe a string limpa (somente dígitos, 11 caracteres).
    """
    if len(cpf) != 11 or not cpf.isdigit():   # rejeita se não tiver 11 dígitos
        return False
    if len(set(cpf)) == 1:                    # rejeita sequências repetidas (111...1)
        return False

    # ── Primeiro dígito verificador ──
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))  # soma ponderada dos 9 primeiros dígitos
    resto = soma % 11                                       # pega o resto da divisão por 11
    d1 = 0 if resto < 2 else 11 - resto                    # regra: resto < 2 → dígito é 0

    # ── Segundo dígito verificador ──
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10)) # soma ponderada dos 10 primeiros dígitos
    resto = soma % 11
    d2 = 0 if resto < 2 else 11 - resto

    return cpf[9] == str(d1) and cpf[10] == str(d2)        # compara com os dígitos reais do CPF


# ── Classe Cliente ───────────────────────────────────────────────────────────

class Cliente:
    """
    Representa um cliente do banco.
    Atributos públicos:  nome, cpf (somente leitura após criação)
    Atributos privados:  __senha_hash
    """

    def _init_(
        self,
        nome: str,                        # nome completo do cliente
        cpf: str,                         # CPF (com ou sem formatação)
        senha: str,                       # senha em texto plano — será imediatamente convertida em hash
        data_nascimento: date | None = None,  # opcional; sintaxe Union moderna (Python 3.10+)
        email: str = "",                  # opcional; padrão string vazia
    ) -> None:                            # _init_ nunca retorna valor

        cpf_limpo = cpf.replace(".", "").replace("-", "")  # remove pontuação do CPF antes de validar

        if not validar_cpf(cpf_limpo):                     # chama o validador; lança exceção se inválido
            raise ValueError(f"CPF inválido: {cpf}")       # ValueError é a exceção padrão para dados incorretos

        self._nome           = nome.strip().title()         # _nome: atributo protegido; .strip() remove espaços, .title() capitaliza cada palavra
        self._cpf            = cpf_limpo                    # _cpf: atributo protegido; armazena somente dígitos
        self._senha_hash    = self._hash(senha)            # __senha_hash: name mangling → vira _Cliente_senha_hash; nunca guarda a senha original
        self.data_nascimento = data_nascimento              # público; pode ser None
        self.email           = email.strip().lower()        # público; normalizado para minúsculas
        self.ativo           = True                         # todo cliente começa ativo por padrão


    # ── Properties ──────────────────────────────────────────────────────────

    @property                              # getter: transforma o método em atributo de leitura
    def nome(self) -> str:
        return self._nome                  # devolve o atributo protegido

    @nome.setter                           # setter: permite "cliente.nome = 'João'" com validação
    def nome(self, valor: str) -> None:
        if not valor.strip():              # rejeita strings vazias ou só com espaços
            raise ValueError("Nome não pode ser vazio.")
        self.nome = valor.strip().title() # reatribui com a mesma normalização do __init_

    @property
    def cpf(self) -> str:
        """Retorna CPF formatado: 999.999.999-99"""
        c = self._cpf                            # alias local para legibilidade
        return f"{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}"  # fatias de string para montar a máscara

    @property
    def cpf_raw(self) -> str:              # property sem setter → somente leitura
        return self._cpf                   # devolve os 11 dígitos sem formatação


    # ── Autenticação ─────────────────────────────────────────────────────────

    @staticmethod                          # método estático: não acessa self nem cls; funciona como função avulsa dentro da classe
    def _hash(senha: str) -> str:
        return hashlib.sha256(            # algoritmo SHA-256 produz digest de 256 bits
            senha.encode()                # converte str → bytes (UTF-8 por padrão)
        ).hexdigest()                     # retorna o hash como string hexadecimal de 64 caracteres

    def autenticar(self, senha: str) -> bool:
        """Retorna True se a senha confere com o hash armazenado."""
        return self.__senha_hash == self._hash(senha)  # compara hash armazenado com hash da senha fornecida

    def alterar_senha(self, senha_atual: str, nova_senha: str) -> None:
        if not self.autenticar(senha_atual):           # só permite troca se a senha atual estiver correta
            raise PermissionError("Senha atual incorreta.")   # PermissionError sinaliza acesso negado
        if len(nova_senha) < 4:                        # regra mínima de segurança
            raise ValueError("Nova senha deve ter pelo menos 4 caracteres.")
        self.__senha_hash = self._hash(nova_senha)     # atualiza o hash com a nova senha


    # ── Representação ────────────────────────────────────────────────────────

    def _str_(self) -> str:
        # _str_ é chamado por print() e str(); voltado para o usuário final
        status = "✅ Ativo" if self.ativo else "🔒 Inativo"   # expressão ternária para definir o texto de status
        return f"Cliente: {self._nome} | CPF: {self.cpf} | {status}"  # usa self.cpf (formatado via property)

    def _repr_(self) -> str:
        # _repr_ é chamado no console e em logs; voltado para o desenvolvedor
        return f"Cliente(nome={self._nome!r}, cpf={self._cpf!r})"  # !r aplica repr() à string (adiciona aspas)
