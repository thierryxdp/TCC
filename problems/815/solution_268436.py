def insere(lista_num, n):
    """Função que recebe uma lista ordenada de números inteiros e um número
inteiro 'n'. Como resultado, ela inclui o número na lista na posição correta,
de forma que a lista continue ordenada."""
    """list,int-->list"""
    list.append(lista_num,n)
    return list.sort(lista_num)