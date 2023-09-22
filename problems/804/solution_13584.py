#Função que retorna uma filtragem de uma tupla com quatro elementos inteiros
# int,int,int,int -> tuple
def filtra_pares(p1,p2,p3,p4):
    filtra_pares = ()
    if  (p1%2==0):
         filtra_pares = filtra_pares + (p1,)
    if (p2%2==0):
        filtra_pares = filtra_pares + (p2,)
    if (p3%2==0):
        filtra_pares = filtra_pares + (p3,)
    if (p4%2==0):
        filtra_pares = filtra_pares + (p4,)
    return filtra_pares