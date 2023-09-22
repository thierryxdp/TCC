def qnt_divisores(n): 
    '''função que recebe um numero 'n' e retorna sua quantidade de divisores.
    int -> int'''
    lista_divisores = []
    for x in range (1,n+1): 
        if n%x == 0:
            lista_divisores += [x]
    return len(lista_divisores)