from Perguntas import Perguntas
from database.Database import Database

COL_STATUS = 0
COL_POSITIVO = 1
COL_NEGATIVO = 2


class Motor:
    def __init__(self):
        db = Database()
        self.db = db.get('motor')
        if not len(self.db):
            print(f'Falha ao carregar a tabela: motor')
            exit(1)
        self.row = self.db[0]
        self.perguntas = Perguntas()
        self.resultado = [
            ['falha_rede', 'falha na rede elétrica'],
            ['falha_instalacao', 'falha na instalação elétrica'],
            ['falha_dimensionamento', 'falha de dimensionamento do motor'],
            ['defeito_motor', 'defeito no motor'],
            ['falha_mecanica', 'falha mecânica']
        ]

    def status_final(self):
        return not bool(self.row[COL_POSITIVO] and self.row[COL_NEGATIVO])

    def get_status(self):
        return self.row[COL_STATUS]

    def get_resultado(self):
        resultado = next(x[1] for x in self.resultado if x[0] == self.get_status())
        return resultado if resultado else self.get_status()

    def pergunta(self):
        pergunta = self.perguntas.get(self.get_status())
        resp = input(pergunta + '? (s/n) ').upper()

        # Em caso de resposta inválida, mantém o status
        proximo = self.row[COL_STATUS]

        if resp == 'S':
            proximo = self.row[COL_POSITIVO]
        elif resp == 'N':
            proximo = self.row[COL_NEGATIVO]
        # print(proximo)
        self.row = next(x for x in self.db if x[COL_STATUS] == proximo)
