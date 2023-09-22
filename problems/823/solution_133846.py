def faltante(L):
    i = 0
    n_numeros = []
    while i <= len(L)+1:
        n_numeros+=[i]
        i+=1
        
    k = 0
    while k < len(L):
        if L[k] in n_numeros:
            index = n_numeros.index(L[k])
            n_numeros.pop(index)
        i+=1
        
        
    return n_numeros