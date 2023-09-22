def filtra_pares(elem1,elem2,elem3,elem4):
    "função que recebe uma tupla com 4 elementos inteiros e retorna apenas os números pares da tupla original."
    a=filtra_pares[0]%2==0
    b=filtra_pares[1]%2==0
    c=filtra_pares[2]%2==0
    d=filtra_pares[3]%2==0
    if a or b or c or d:
        return (a,b,c,d)