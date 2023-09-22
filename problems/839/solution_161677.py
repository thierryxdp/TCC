def carro(pessoas, capacidade):
    '''retorna o número de carros necessários para a viajem, levando em consideração o número de pessoas e a capacidade do(s) carro(s)'''
    if (capacidade >= 0):
        return pessoas//capacidade
    else:
        return pessoas//5