def insere(lista_numero,n):
    '''Função que dada uma lsta crescente de números inteiros e um número inteiro n, inclui n na posição correta;
       list->list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero