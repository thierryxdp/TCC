def repetidos(numeros):
    i=1
    resposta=0
    while i < len(numeros):
        if numeros[i] == numeros[i-1]:
            resposta= resposta +1
        i= i+1
    return resposta