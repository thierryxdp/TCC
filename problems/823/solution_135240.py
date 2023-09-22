def faltante(lista):
    i = 0
    peca_faltante = []
    lista.sort()    # deveras importante colocar a lista em ordem crescente
    while i<len(lista)-2:
        if lista[i]-lista[i+1]!=1:
            peca_faltante = peca_faltante + [lista[i]]
    i = i+1
    return peca_faltante