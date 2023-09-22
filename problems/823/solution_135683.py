def faltante(L):
    copia_lista = lista[:]
    total_pecas = len(copia_lista)+1
    i = 1
    peca_faltante = 0
    pecas_totais = []
    
    while i<len(total_pecas):
        if i==lista.index(i):
            pecas_totais = pecas_totais + [[i],]
        elif i!=lista.index(i):
            peca_faltante = i
        i = i+1
    return i