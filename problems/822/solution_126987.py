def repetidos (lista):
    '''uma função que retorna o número de vezes que um elemento é igual ao
    anterior. lista -> int'''
    resposta = 0
    contador = 0
    posicao = 0
    while contador < len(lista)-1:
        if lista [contador] == lista[contador+1]:
            resposta += 1
        posicao += 1
        contador += 1
    return resposta