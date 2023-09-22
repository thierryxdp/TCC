def repetidos(lista):
    '''Dada uma lista de números, retorna o número de vezes
    que um elemento da lista é igual ao elemento anterior.
    list -> int'''
    elemento = 1
    resposta = 0
    while elemento < len(lista):
        if lista[elemento]==lista[elemento-1]:
            resposta = resposta + 1
        elemento = elemento + 1
    return resposta