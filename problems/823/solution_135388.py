def faltante(lista):
    listai= len(lista)+1
    i=1
    pecas=[i]
    while i<listai:
        pecas+=[(i+1),]
        i=i+1
    totalpecas= sum(pecas)
    totalcaixa= sum(listai)
    faltando= totalpecas-totalcaixa