def repetidos(numeros):
    '''função que recebe uma lista de numeros e retorna 
    quantos números se repetem'''
    contador = 0
    resposta = 0
    while contador < len(numeros):
        if numeros[contador] == numeros[contador - 1]:
            resposta = resposta  + 1
    	contador = contador + 1
    return resposta