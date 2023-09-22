def faltante(lista):
    i=0
    seq=list(range(1,len(lista)+2))
    while i<len(lista):
        if seq[i] not in lista:
            return seq[i]
        i=i+1