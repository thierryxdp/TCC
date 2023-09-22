def repetidos(numeros):
    i=0
    resposta=0
    while i <= len(numeros):
        if numeros[i] == numeros[1+i]:
            resposta= resposta +1
        i= i+1
    return resposta