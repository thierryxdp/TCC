def repetidos(lista):
    """"Esta função recebe uma lista e retorna a quantidade de vezes em que um elemento da lista é igual ao anterior.
    list -> int"""
    acumulador = 0
    for i in lista:
        posicao = lista.index(i)-1
        if i == lista[posicao]:
            acumulador += 1
   	return acumulador