def repetidos(lista):
    qtd=0
    y=1
    for x in lista:
        if lista[y]==lista[y-1]:
            qtd+=1
        y+=1
    return qtd