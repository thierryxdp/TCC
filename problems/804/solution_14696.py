#Função que recebe uma tupla com quatro elementos e retorna uma nova tupla apenas com os elementos pares
#tup -> tup
def filtra_pares(t):
    if t[0]%2==0:
        return t[1]
    elif t[1]%2==0:
        return t[1]