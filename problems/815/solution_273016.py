def insere(lista_numero,n):
    """Função, que dada uma lista ordenada(crescente) de números inteiros e n um número inteiro, retorna o n na posição correta, mantendo a lista ordenada."""
    """list,int->list"""
    lista = lista_numero + [n]
    list.sort(lista)
    return lista