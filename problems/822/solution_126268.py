def repetidos(lista_num):
    '''Retorna a quantidade de vezes em que
    o número na lista é igual ao seu antecessor
    list --> int'''
    i=1
    qntd=0
    while i < len(lista_num):
        if lista_num[i] == lista_num[i-1]:
            qntd += 1
        i += 1
    return qntd