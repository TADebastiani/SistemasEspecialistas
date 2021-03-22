class Perguntas:
    def __init__(self):
        self.level = [
            ['Seu Pet está agitado?', 'agitado'],
            ['O seu Pet está comendo bem?', 'alimentado'],
            ['O ambiente é adequado?', 'ambiente_adequado'],
            ['O seu Pet fez atividade física?', 'se_movimenta'],
            ['Dispositivo de proteção está recebendo a tensão correta'],
            ['Dispositivo de proteção está com o ajuste de corrente correto (Corrente nominal * fator de serviço)'],
            ['Existe algum curto circuito entre o contator e o dispositovo de proteção'],
            ['Existe algum curto circuito entre motor e o contator'],
            ['Todos os cabos do motor estavam conectados nos seus devidos lugares'],
            ['O motor é novo'],
            ['Rotor do motor está bloqueado'],
            ['Os rolamentos do motor foram trocados'],
            ['Estrutura mecânica está bloqueada ou exercendo esforço excessivo'],
            ['Aplicação que o motor está sendo utilizado é nova'],
            ['Todas as conexões estão devidamente conectadas'],
        ]

    def proxima(self):
        pergunta = self.level[0]
        del self.level[0]
        return pergunta
