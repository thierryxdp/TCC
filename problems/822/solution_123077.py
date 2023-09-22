def repetidos(lista_num):
    """"Esta função recebe uma lista e retorna a quantidade de vezes em que um elemento da lista é igual ao anterior.
    list -> int"""
    while len(lista_num) <= 10:
        contador = 1
    	if lista_num[contador] == lista_num[contador - 1]:
            contador += 1
    return contador