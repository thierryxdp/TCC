def faltante(lista):
    i=0
    while i<len(lista):
    if len(lista)==1 and lista[i]==1:
            return 2
    else:
        return 1
    
    if lista[i]+1!=lista[i+1]:
        return lista[i]+1
    i=i+1