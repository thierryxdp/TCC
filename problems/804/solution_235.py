def filtra_pares(tup):
    """Recebe uma tupla com quatro elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os pares; tup -> tup"""
    n1 = tup[0]
    n2 = tup[1]
    n3 = tup[2]
    n4 = tup[3]
    if n1%2==0 and n2%2==0 and n3%2==0 and n4%2==0:
        return n1, n2, n3, n4
    elif n1%2!=0 and n2%2==0 and n3%2==0 and n4%2==0:
        return n2, n3, n4
    elif n1%2==0 and n2%2!=0 and n3%2==0 and n4%2==0:
        return n3, n4
    elif n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2==0:
        return n4
    elif n1%2==0 and n2%2!=0 and n3%2!=0 and n4%2!=0:
        return n1
    elif n1%2==0 and n2%2==0 and n3%2==0 and n4%2!=0:
        return n1, n2, n3
    elif n1%2==0 and n2%2!=0 and n3%2==0 and n4%2!=0:
        return n1, n3
    elif n1%2==0 and n2%2==0 and n3%2!=0 and n4%2!=0:
        return n1, n2