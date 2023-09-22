def fatorial(x):
    '''Dado um número x, a função retorna o fatorial desse número
    float -> float'''
    
    i = 0 
    lista = ()
 
    while x > i:
        if lista != ():
        t = (x * lista), 
        lista = lista + t
        x = x - 1
        i = i + 1
        str.replace(lista,lista[0],t)
    return lista[0]