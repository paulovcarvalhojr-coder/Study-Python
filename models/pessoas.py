# ── Imports ─────────────────────────────────────────────────────────────────
from datetime import date  # tipo date para representar data de nascimento

class Pessoa:

    def __init__(
        self,
        nome: str,
        cpf: str,
        dt_nasc: date,
        end: str,
        email: str = "",
    ) -> None:

        self._nome = nome.strip().title()
        self._cpf = self.validar_cpf(cpf) #funçao criada abaixo
        self._dt_nasc = dt_nasc
        self._end = end.strip()
        self._email = email.strip()

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        cpf_limpo = cpf.replace(".", "").replace("-", "")  # remove pontuação do CPF antes de validar
        if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():  # rejeita se não tiver 11 dígitos
            return False
        if len(set(cpf_limpo)) == 1:  # rejeita sequências repetidas (111...1)
            return False

        soma = 0
        peso = 10
        for i in range(9): # puxa os primeiros 9 dígitos
            soma += int(cpf_limpo[i]) * peso # multiplica o dígito pelo peso
            peso -=1 # diminui o peso, conforme for passando de dígito (1º x 10, 2º x 9 e assim sucessivamente)

        resultado = (soma * 10) % 11
        if resultado == 10:
            resultado = 0

        if resultado != int(cpf_limpo[9]):
            return False

        soma = 0
        peso = 11
        for i in range(10): # puxa os primeiros 10 dígitos
            soma += int(cpf_limpo[i]) * peso # multiplica o dígito pelo peso
            peso -=1 # diminui o peso, conforme for passando de dígito (1º x 11, 2º x 10 e assim sucessivamente)

        resultado = (soma * 10) % 11
        if resultado == 10:
            resultado = 0

        if resultado != int(cpf_limpo[10]):
            return False
        return cpf_limpo

    @property  # getter: transforma o método em atributo de leitura
    def nome(self) -> str:
        return self._nome


class Cliente(Pessoa):

    def __init__(
        self,
        nome: str,
        cpf: str,
        dt_nasc: date,
        end: str,
        email: str,
        status_cliente: bool,
        dt_cadastro: date,
        renda_decl: float,

    ) -> None:

        super().__init__(nome, cpf, dt_nasc, end, email)

        self.status_cliente = status_cliente
        self.dt_cadastro = dt_cadastro
        self.renda_decl = renda_decl

class Funcionario(Pessoa):

    def __init__(
            self,
            nome: str,
            cpf: str,
            dt_nasc: date,
            end: str,
            email: str,
            id: int,
            cargo: str,
            dpto: str,
            dt_admissao: str,
            salario: float,
            status: str,



    ) -> None:
        super().__init__(nome, cpf, dt_nasc, end, email)

        self.id = id
        self.cargo = cargo.strip()
        self.dpto = dpto.strip()
        self.dt_admissao = dt_admissao
        self.salario = salario
        self.status = status.strip()