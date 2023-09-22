def repetidos(lista):
    tamanho=len(lista)
    indice=0
    novalista=[]
    while indice < tamanho:
        novalista+=lista[indice]
        indice+=1
    return indice