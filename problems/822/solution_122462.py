def repetidos(lista):
    qtd=0
    for x in lista:
        y=x+1
        if x==lista[y]:
            qtd+=1
    return qtd