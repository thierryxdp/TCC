#Start your python function here
def filtra_pares(a,b,c,d):
    'Recebe uma tupla com quatro elementos inteiros, retorna uma tupla com apenas os elementos pares da tupla original'
    tupla=()
    if a%2==0:
        tupla=(a)
    if b%2==0:
        tupla=(a,b)
    if c%2==0:
        tupla=(a,b,c)
    if d%2==0:
        tupla=(a,b,c,d)
    return tupla