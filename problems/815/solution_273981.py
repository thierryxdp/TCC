def insere(lista_numero, n):
    '''Função que insere um número inteiro n na 
    posição correta da lista crescente de numeros inteiros
    valores: list, int --> list'''
    lista_numero = lista_numero.append(n)
    return lista_numero.sort()