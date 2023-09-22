def filtra_pares(tupla):
    'Dado um conjunto com quatro números inteiros, retorna apenas os pares. Entrada; tupla(int,int,int,int). Saída: tupla(int).'
    n1=tupla[0]
    n2=tupla[1]
    n3=tupla[2]
    n4=tupla[3]
    if (n1%2)==0:
        return True
    elif (n2%2)==0:
        return True
    elif (n3%2)==0:
        return True
    elif (n4%2)==0:
        return True
    else:
        return False
    list(filter(filtra_pares, (n1,n2,n3,n4)))