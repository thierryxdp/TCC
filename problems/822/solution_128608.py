def repetidos(lista):
    contador=1
    repeticoes=0
    while contador<len(lista):
        if lista[contador]==lista[contador-1]:
            repeticoes+=1
            contador+=1
        else:
            contador+=1
    return repeticoes