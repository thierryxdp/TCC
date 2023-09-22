def insere(lista_numero,n):
    """Função que dada uma lista ordenada(crescente) inclui um numero na posicao
correta; list,int -> list"""
    lista=lista_numero+[n]
    list.sort(lista)
    return lista