def repetidos(lista):
    indice=1
    tamanho=len(lista)-1
    cont=0
    while indice<=tamanho:
        if lista[indice]==lista[indice-1]:
            cont+=1
        indice+=1    
    return cont