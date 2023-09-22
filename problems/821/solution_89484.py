def fatorial(n):
    '''
        Funcao recebe um numero e
        retorna o seu fatorial
        int -> int
        
    '''

    i = 0
    lista = []

    while n > len(lista):
        lista = lista + [n - i,]
        i = i + 1

    c = 0
    fatorial = 1

    while c < len(lista):
        fatorial = fatorial*lista[c]
        c = c + 1
        
    return fatorial