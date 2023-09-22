def repetidos(numeros):
    indice=1
    resposta=0
    while indice <= len(numeros):
        if numeros[indice-1] == numeros[indice]:
            resposta= resposta +1
        indice= indice +1
    return resposta