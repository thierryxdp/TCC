def carros(pessoas,capacidade=5):
    '''função que retorna o número exato de carros
    necessários para uma viagem dados o número de
    pessoas e a capacidade do carro (caso necessite)'''
    return .ceil(pessoas/capacidade)