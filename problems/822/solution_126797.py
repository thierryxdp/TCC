def repetidos(lista):
    i=len(lista)
    qtd=0
    while i>0:
        if lista[i]==lista[i-1]:
            qtd+=1
        i-=1
    return qtd