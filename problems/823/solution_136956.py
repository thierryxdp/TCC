def faltante(lista):
    y = lista[:]
    list.sort(y)
    ontagem = 0 
    peca = -1
    while contagem < len (y):
        if y[contagem] == contagem +1:
            contagem +=1
        else:
            peca = montagem +1 
            contagem+len (y)
        if peca ==-1:
            contagem = len(y)+1
    return peca