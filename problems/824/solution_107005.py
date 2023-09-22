def repetidos(lista_de_numeros):
    ''' Função que recebe como entrada uma lista de número e retorne o número
        de vezes que um elemento da lista é igua ao elemento anterior.
        lista ---> int'''
    resposta = 0
    contador = 0
    posicao = 0
    while contador < len(lista_de_numeros) - 1:
        if lista_de_numeros[posicao] == lista_de_numeros[posicao + 1]:
            resposta = resposta + 1
        contador = contador + 1
        posicao = posicao + 1
    return resposta