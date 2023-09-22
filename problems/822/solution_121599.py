def repetidos(lista_num):
    '''Função que recebe uma lista e retorna o número de veses que um elemento da
lista é igual ao elemento anterior
    list -> int
    '''
    contador = 1
    resposta = 0
    while contador < len(lista_num):
        if lista_num[contador] == lista_num[contador-1]:
            resposta += 1
        contador +=1
    return resposta