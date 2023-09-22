def insere (lista_numero,n):
    """Função que dada uma lista ordenada(crescente) de números inteiros e um número inteiro n, inclua n na posição correta, de tal maneira que ela continue ordenada"""
    """list,int->list"""
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    return lista_numero