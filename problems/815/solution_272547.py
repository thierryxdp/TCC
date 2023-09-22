def insere(lista_numero,n):
    '''função que insere o número inteiro n na posição
    adequada numa lista crescente
    valor de entrada: list, int
    valor de saída: list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero