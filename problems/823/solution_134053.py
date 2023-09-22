def faltante(lista):
    '''
    '''
    contador = 1
   	lista.sort()
    while contador < len(lista):
        if lista[contador] != (lista[contador-1] + 1):
            return contador
        contador += 1