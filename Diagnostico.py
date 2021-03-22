from Base import Base


class Diagnostico(Base):
    def __init__(self):
        super().__init__('pet')
        #self.resultado = ['cansado', 'estressado', 'deprimido', 'faminto', 'saudavel']
        self.resultado = ['falha_rede_eletrica', 'falha_instalacao', 'falha_dimensionamento', 'motor_defeito', 'falha_mecanica']


"""
O seu Pet está agitado?'			->		'agitado'
O seu Pet está comendo bem?'		->		'alimentado'
'O ambiente é adequado?'			->		'ambiente_adequado'
'O seu Pet fez atividade física?' 	-> 		'se_movimenta',		
"""
