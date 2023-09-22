def repetidos(lista):
    qtd=0
    y=x+1
    for x in lista:
        if x==lista[y]:
            qtd+=1
    return qtd