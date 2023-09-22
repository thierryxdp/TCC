def filtra_pares(tupla):
    'Dado um conjunto com quatro números inteiros, retorna apenas os pares. Entrada; tupla(int,int,int,int). Saída: tupla(int).'
    pares=()
    n1=tupla[0]
    n2=tupla[1]
    n3=tupla[2]
    n4=tupla[3]
    if (n1%2)==0:
        pares=pares+(tupla[0],)
    if (n2%2)==0:
        pares=pares+(tupla[1],)
    if (n3%2)==0:
        pares=pares+(tupla[2],)
    if (n4%2)==0:
        pares=pares+(tupla[3],)
    return pares