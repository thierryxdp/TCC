def repetidos(numeros):
    indice=0
    resposta=0
    while indice < len(numeros):
        if numeros[indice] == numeros[indice+1]:
            resposta= resposta +1
        indice= indice +1
    return resposta