def insere(lista_num, n):
    """Função que recebe uma lista ordenada de números inteiros e um número
inteiro 'n'. Como resultado, ela inclui o número na lista na posição correta,
de forma que a lista continue ordenada."""
    """list,int-->list"""
    resultado=[]
     for c in lista_num:
        if c > n:
            resultado.append(c)
    return list.sort(resultado)