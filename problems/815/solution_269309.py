def insere(lista_numero,n):
    """Esta função recebe uma lista de números inteiros em ordem crescente e um número inteiro e acrescenta este número na lista de forma que a lista continue na ordem crescente
    list,int -> int"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero