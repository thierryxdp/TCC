def faltante(n):
    lista = [*range(1,len(n)+1,1)]
    i = 0
    while i < len(n):
        if lista[i] in n:
            i = i+1
        else:
            return lista[i] 
    return len[n]+1