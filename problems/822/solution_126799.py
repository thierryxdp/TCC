def repetidos(lista):
    i=0
    qtd=0
    while i<len(lista):
        a=lista[i]
        i+=1
        if(i==len(lista)):
            return qtd
        if (a==lista[i]):
            qtd+=1