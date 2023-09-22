def repetidos(lista_num):
    """"Esta função recebe uma lista e retorna a quantidade de vezes em que um elemento da lista é igual ao anterior.
    list -> int"""
    contador = 0
    posicao = 0
    while lista_num[posicao] < 958:
    	if lista_num[posicao] == lista_num[posicao - 1]:
            contador += 1
            posicao += 1
    return contador