#Start your python function here
    '''Função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla
contendo apenas os elementos pares da tupla original, na mesma ordem que se encontravam
    tupla(int,int,int,int) -> tupla
    '''
    if tupla[0]//2==tupla[0]/2:
        a = tupla[0]
    else:
        a = None
    if tupla[1]//2==tupla[1]/2:
        b = tupla[1]
    else:
        b = None
    if tupla[2]//2==tupla[2]/2:
        c = tupla[2]
    else:
        c = None
    if tupla[3]//2==tupla[3]/2:
        d = tupla[3]
    else:
        d = None
    return (a,b,c,d)