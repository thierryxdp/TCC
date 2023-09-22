def maiores(lista,numero):
    ''' Funcao que dada uma lista e um numero, ela retorna uma lista
    	com todos os numeros maiores que o numero dado list >>> list'''
    lista.append(numero)
    lista.sort()
    posicao_numero = lista.index(numero)
    return lista[posicao_numero+1:]