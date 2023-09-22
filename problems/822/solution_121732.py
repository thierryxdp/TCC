def repetidos(lista):
    contador=0
    resposta=0
    while contador < len(lista)-1:
        if lista[contador] == lista[contador+1]:
            resposta+= 1
    return resposta