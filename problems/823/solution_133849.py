def faltante(L):
    i = 0
    n_numeros = list(range(len(L)+1))

        
    k = 0
    while k < len(L):
        if L[k] in n_numeros:
            index = n_numeros.index(L[k])
            n_numeros.pop(index)
        k+=1
        
        
    return n_numeros[0]