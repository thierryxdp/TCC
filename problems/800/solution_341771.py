def total(lista_comp,produtos):
    total=0
    i=0
    while i < len(produtos):
        if lista_comp[i] in produtos.values():
            total=total+lista_comp[i]
            i+=1
    return total