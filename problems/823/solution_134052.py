def faltante(lista):
    '''
    '''
    contador = 1
    lista_nova = lista.sort()
    while contador < len(lista):
        if lista_nova[contador] != (lista_nova[contador-1] + 1):
            return contador
        contador += 1