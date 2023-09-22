def faltante(L):
    i = 0
    n_numeros = list(range(1,len(L)+2))

        
    k = 0
    while k < len(L):
        if L[k] in n_numeros:
            index = n_numeros.index(L[k])
            n_numeros.pop(index)
        k+=1
        
        
    return n_numeros[0]