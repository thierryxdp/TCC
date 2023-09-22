def repetidos(lista):
    qtd=0
    for x in lista:
        if x==lista[x+1]:
            qtd+=1
    return qtd