def insere(lista_numero,n):
    """Função que dada uma lista ordenada(crescente) inclui um numero na posição
correta; list,int -> list"""
    lista_nova= lista_numero+[n]
    lista_ordenada= list.sort(lista_nova)
    return lista_ordenada