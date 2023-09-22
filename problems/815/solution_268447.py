def insere(lista_numero, n):
    """Função que recebe uma lista ordenada de números inteiros e um número
inteiro 'n'. Como resultado, ela inclui o número na lista na posição correta,
de forma que a lista continue ordenada."""
    """list,int-->list"""
    resultado=[]
    resultado=list.append(lista_numero,n)
    list.sort(resultado)
    return resultado