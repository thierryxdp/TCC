def filtra_pares(a,b,c,d):
    """recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla apenas com os elementos pares da tupla"""
    t=[a,b,c,d]
    li = []
    for x in t:
        if x%2 == 0:
            li.append(x)
            return (li)