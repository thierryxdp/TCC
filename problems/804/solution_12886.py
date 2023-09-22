# Recebe uma tupla com quatro elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesa ordem em que se encontravam.
def filtra_pares((a)):
    a1 = (a, )
    b1 = (b, )
    c1 = (c, )
    d1 = (d, )
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return a1 + b1 + c1 + d1
    elif a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return a1 + b1 + c1