def repetidos(lis):
    '''recebe um lista 'lis' e retorma o numero de vezes que p valor
    de uma posição da lista é igual ao valora anterior a ele
    lis------>int'''
    i = 1
    rep = 0
    while(i<len(lis)):
        if(lis[i] == lis[i-1]):
            rep = rep + 1
            i += 1
        else:
            i += 1
    return rep