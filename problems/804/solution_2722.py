#retorna uma tupla contendo apenas os elementos pares da tupla de entrada
#tupla de entrada ddeve conter 4 elementos inteiros apenas
#tup->tup

def filtra_pares(tup):
    pares =()
    if int(tup[1])%2==0:
        pares = pares+(int(tup[1]),)
    if int(tup[2])%2==0:
        pares = pares+(int(tup[2]),)
    if int(tup[3])%2==0:
        pares = pares+(int(tup[3]),)
    if int(tup[4])%2==0:
        pares = pares+(int(tup[4]),)
    return pares