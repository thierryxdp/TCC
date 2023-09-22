def repetidos(lista):
    qtd=0
    y=1
    for x in lista[:-1]:
        if lista[y-1]==lista[y]:
            qtd+=1
        y+=1
    return qtd