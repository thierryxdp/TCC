def repetidos(lista):
    '''Essa função recebe uma lista de numeros como entrada, e retorna o numero de 
    vezes que um elemento da lista é igual ao elemento anterior
    list -> int'''
    anterior = atual = contador = vezes = 0
    while contador < len(lista):
        if contador == 0:
            atual = lista[contador]
        else:
            atual = lista[contador]
            if anterior == atual:
                vezes += 1
        anterior = atual
        contador += 1
    return vezes