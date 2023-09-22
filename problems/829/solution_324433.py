def soma_h(numero):
    '''funçao que retorna o valor de uma funçao de n termos
    inteiros;
    int -> int/float'''
    s = 0
    for i in range(numero):
        s += ((1)/(1+i))
    return round(s,2)