def maiores(numeros, n):
    '''
    '''
    nova_lista = numeros[:]
    nova_lista.append(n)
    nova_lista.sort()
    indice = nova_lista.index(n)
    return nova_lista[indice+1:]