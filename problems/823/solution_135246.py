def faltante(lista):
    i = 0
    peca_faltante = []
    lista.sort()    # deveras importante colocar a lista em ordem crescente
    while i<len(lista)-1:
        if lista[i]-lista[i+1]!=1:
            peca_faltante = peca_faltante + [lista[i],]
        else:
            return lista[i]-1
    i = i+1
    return peca_faltante