def repetidos(listaNumeros):
    '''Dada uma lista de numeros, retorna a quantidade de vezes que um elemento é igual ao seu anterior.
    list -> int'''
    anterior = -1
    atual = 0
    vezes = 0
    i = 0

    while i < len(listaNumeros):
        if listaNumeros[atual] == listaNumeros[anterior]:
            vezes +=1
        anterior += 1
        atual += 1
        i += 1
    return vezes