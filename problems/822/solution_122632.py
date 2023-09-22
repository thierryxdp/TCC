def repetidos(lista):
    contador=1
    tamanho=len(lista)
    cont=0
    while contador<tamanho:
        if lista[contador]==lista[contador+1]:
            cont+=1
    return cont