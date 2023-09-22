def repetidos(lista):
    contador=0
    i=0
    soma=0
    while contador<len(lista):
        if lista[i]==lista[i+1]:
            contador+=1
            soma+=1
    return soma