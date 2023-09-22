def repetidos(lista):
    "função que recebe uma lista de numeros e retorna o numero(int) de vezes que um elemento da lista se repetiu"
    posicao = 0
    contagem = 0
    while posicao < len(lista):
        if lista[posicao] == lista[posicao+1]:
            contagem += 1
            if posicao == list.index(lista,lista[-1]):
                return contagem
        posicao += 1