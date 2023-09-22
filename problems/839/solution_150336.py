def carros(pessoas, capacidade=5):
    import math
    ''' retorna o numero exato de carros necessarios para uma viagem dado a quantidade de pessoas. se os veiculos forem considerados nao convencionais, sera dado tambem como parametro de entrada a capacidade deles'''
    ''' int, int-> int'''
    return math.ceil(pessoas/capacidade)