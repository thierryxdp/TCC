def repetidos(lista_num):
    '''Função que recebe como entrada uma lista de números
    e retorna o número de vezes que um elemento da lista é igual
    ao anterior. list->int'''
    i=0
    resposta=0
    while i<len(lista_num):
        if lista_num[i]==lista_num[i-1]:
            resposta+=1
        i+=1
    return resposta