def total(lista_comp,produtos):
    total=0
    totalf=0
    for i in range(0,len(produtos)):
        if lista_comp[i] == produtos.keys():
            total=total+lista_comp[i][0]
            totalf=round(total,2)
            return totalf