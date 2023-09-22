def num_bombons(dinheiro, preco_bombom):
    ''' funcao que calcula a quantidade de bombons dado o dinheiro e o preco'''
    ''' float, float -> int'''
    calculo=dinheiro/ preco_bombom
    return round(calculo)