#Recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla contendo
#somente os elementos pares da tupla original
#tupla -> tupla
def filtra_pares(n):
    n1 = int(n[0])
    n2 = int(n[1])
    n3 = int(n[2])
    n4 = int(n[3])
    nova_tupla = []
    if n1%2==0:
        nova_tupla.append(n1)
    if n2%2==0:
        nova_tupla.append(n2)
    if n3%2==0:
        nova_tupla.append(n3)
    if n4%2==0:
        nova_tupla.append(n4)
    return nova_tupla