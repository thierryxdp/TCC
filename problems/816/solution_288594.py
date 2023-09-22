def maiores(lista,n):
    """recebe uma lista um inteiro e retorna uma nova lista
    contendo os inteiros maiores que n em ordem crescente"""
    l=[]
    for x in lista:
        if x>n:
            l.append(x)
    l.sort()
    return l