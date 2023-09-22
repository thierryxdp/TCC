def repetidos(lista_num):
    """"Esta função recebe uma lista e retorna a quantidade de vezes em que um elemento da lista é igual ao anterior.
    list -> int"""
    contador = 0
    for i in lista_num:
        posicao = i.find()
        if i == lista_num[posicao - 1]:
            contador += 1
    return contador