def repetidos(lista):
    i=0
    qtd=0
    while i<len(lista):
        if lista[i]==lista[i+1]:
            qtd+=1
        i+=1
    return qtd