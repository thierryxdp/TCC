def faltante(lista):
    copia_lista = lista[:]
    total_pecas = len(copia_lista)+1 # pq esta faltando uma peca
    i = 1
    peca_faltante = []
    pecas_totais= [] 
    while i<len(lista):
        if i==lista.index:
            peca_totais = pecas_totais + [[i],]
        i = i +1 
    return i