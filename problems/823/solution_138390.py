def faltante(lista=[]):
    lista.sort()
    if len(lista)==1 and lista[0]!=1:
        return 1
    
    for i in range(len(lista)):
        if lista[i]!=i+1:
            return i+1
    return len(lista)+1