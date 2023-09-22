def fatorial(x):
    '''Dado um número x, a função retorna o fatorial desse número
    float -> float'''
    
    i = 0 
    lista = [x]
    while x > i:
        if lista[0] != x* (x-1):
            t = x - i
            list.append(lista,t)
        x = x - 1
        i = i + 1
    return lista[0]