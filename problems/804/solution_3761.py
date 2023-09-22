def filtra_pares(tupla):
    'Dado um conjunto com quatro números inteiros, retorna apenas os pares. Entrada; tupla(int,int,int,int). Saída: tupla(int).'
    pares=(,)
    n1=tupla[0]
    n2=tupla[1]
    n3=tupla[2]
    n4=tupla[3]
    if (n1%2)==0:
        pares=pares+n1
    if (n2%2)==0:
        pares=pares+n2
    if (n3%2)==0:
        pares=pares+n3
    if (n4%2)==0:
        pares=pares+n4
    return pares