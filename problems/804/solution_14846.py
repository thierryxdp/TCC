#Função que recebe uma tupla com quatro elementos e retorna uma nova tupla apenas com os elementos pares
#tup -> tup
def filtra_pares(t):
    if t[1]%2!=0 and t[2]%2!=0 and t[3]%2!=0 and t[4]%2!=0:
        return ()
    elif t[1]%2==0 and t[2]%2!=0 and t[3]%2!=0 and t[4]%2!=0:
        return t[1]
    elif t[1]%2==0 and t[2]%2==0 and t[3]%2!=0 and t[4]%2!=0:
        return t[1],t[2]
    elif t[1]%2==0 and t[2]%2==0 and t[3]%2==0 and t[4]%2!=0:
        return t[1],t[2],t[3]
    elif t[1]%2==0 and t[2]%2==0 and t[3]%2==0 and t[4]%2==0:
        return t
    elif t[1]%2!=0 and t[2]%2==0 and t[3]%2==0 and t[4]%2==0:
        return t[2],t[3],t[4]
    elif t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0 and t[4]%2==0:
        return t[3],t[4]