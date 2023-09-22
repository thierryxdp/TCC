def insere(lista_numero,n):
    '''função que insere o número inteiro n na posição
    adequada numa lista crescente
    valor de entrada: list, int
    valor de saída: list'''
    inserida= lista_numero.append(n)
    crescente= list.sort(inserida)
    return crescente