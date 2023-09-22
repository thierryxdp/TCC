def ordem(lista,n):
    """função que recebe uma lista crescente de números inteiros e um número inteiro n
    e retorna a mesma lista com n na posiçao correta. list, int -> list"""
    novalista = list.append(lista,n)
    list.sort(novalista)
    return novalista