def filtraMultiplo(lista, numero):
    i=1
    c=0
    while c< len(lista)-1:
        if lista[i] == lista[c]:
            c +=1
        if c==numero:
            return i
        i +=1
    return -1