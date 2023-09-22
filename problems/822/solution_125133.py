def repetidos(lista):
    n = 0
    vezes = 0
    
    while n <= len(lista):
        if lista[n] == lista[n+1]:
            vezes = vezes + 1
            n = n + 1
        elif lista[n] != lista [n+1]:
                n = n + 1
                
    return vezes