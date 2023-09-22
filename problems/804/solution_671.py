#Recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla contendo
#somente os elementos pares da tupla original
#tupla -> tupla
def filtra_pares(n):
    n1 = int(n[0])
    n2 = int(n[1])
    n3 = int(n[2])
    n4 = int(n[3])
    nova_tupla = ()
    if int(n[0])%2==0:
        tupla1 = (n1,)
        nova_tupla = nova_tupla + tupla1
    if n2%2==0:
        tupla2 = (n2,)
        nova_tupla = nova_tupla + tupla2
    if n3%2==0:
        tupla3 = (n3,)
        nova_tupla = nova_tupla + tupla3
    if n4%2==0:
        tupla4 = (n4,)
        nova_tupla = nova_tupla + tupla4
    return nova_tupla