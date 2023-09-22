from math import ceil
def carros(pessoas,assento=5):
    '''retorna a quantidade de carros necessárias para a viagem do grupo de amigos. int,int-->int|float.'''
    return ceil(pessoas/assento)