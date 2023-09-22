def faltante(lista):
    copia_lista = lista[:]
    total_pecas = len(copia_lista)+1 # pq esta faltando uma peca
    i = 0
    j = 0
    pecas_totais= [] 
    while pecas_totais!=total_pecas:
        pecas_totais = pecas_totais + [i,]
        i = i + 1
    while pecas_totais[i]==copia_lista[i]:
        j = j+1
    return j+1