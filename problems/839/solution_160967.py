def carros(pessoas,capacidade=5):
    '''Calcule e retorne o número exato de carros necessários para uma viagem. Considere como entradas o núumero de pessoas e a capacidade dos veículos'''
 
    carros = int(pessoas/capacidade)
    return carros