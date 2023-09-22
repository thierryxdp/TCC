def insere(lista_numero,n):
    '''Função que dada uma lista ordenada de forma crescente e um número inteiro n, retorna a mesma lista com n incluído a posição correta de tal maneira que a lista continue ordenada: list,int -> list'''
    lista_numero = list.append(lista_numero,n)
    lista_numero = list.sort(lista_numero)
    return lista_numero