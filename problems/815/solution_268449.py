def insere(lista_numero, n):
    """Função que recebe uma lista ordenada de números inteiros e um número
inteiro 'n'. Como resultado, ela inclui o número na lista na posição correta,
de forma que a lista continue ordenada."""
    """list,int-->list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero