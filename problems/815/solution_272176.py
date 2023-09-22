def insere(lista_numero,n):
    """Dado uma lista de números inteiros em ordem crescente, adiciona um número
    à lista na posição correta:
    list,int-->list"""
    lista_numero=lista_numero+[n]
    lista_numero.sort()
    return lista_numero