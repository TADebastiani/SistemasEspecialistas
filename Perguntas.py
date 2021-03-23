class Perguntas:
    def __init__(self):
        self.level = [
            ['Dispositivo de proteção está recebendo a tensão correta','tensao_correta'],
            ['Todas as conexões estão apertadas','conexoes_apertadas'],
            ['Dispositivo de proteção está com o ajuste de corrente correto (Corrente nominal * fator de serviço)','ajuste_corrente'],
            ['Existe algum curto circuito entre o contator e o dispositovo de proteção','curto_contator'],
            ['Existe algum curto circuito entre motor e o contator','curto_motor'],
            ['Todos os cabos do motor estavam conectados nos seus devidos lugares','ligacao_motor'],
            ['O motor é novo','motor_novo'],
            ['Aplicação que o motor está sendo utilizado é nova'],
            ['Estrutura mecânica está bloqueada ou exercendo esforço excessivo','mecanica_travada'],
            ['Rotor do motor está bloqueado','rotor_bloqueado'],
            ['Os rolamentos do motor foram trocados','rolamento_novo'],
        ]

    def proxima(self):
        pergunta = self.level[0]
        del self.level[0]
        return pergunta
