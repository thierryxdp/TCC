#Start your python function here
def filtra_pares(a,b,c,d):
    """função que recebe uma tupla com quatro numeros inteiros e retorne uma nova tupla que tem elementos pares respectivamente; int,int,int,int -> tuple"""
    if ((a%2==0) and (b%2==0) and (c%2==0) and (d%2==0)):
        return a,b,c,d
    elif((a%2!=0) and (b%2==0) and (c%2==0) and (d%2==0)):
        return b,c,d
    elif((a%2==0) and (b%2!=0) and (c%2==0) and (d%2==0)):
         return a,c,d
    elif((a%2==0) and (b%2==0) and (c%2!=0) and (d%2==0)):
         return a,b,d
    elif((a%2==0) and (b%2==0) and (c%2==0) and (d%2!=0)):
         return a,b,c
    elif((a%2!=0) and (b%2!=0) and (c%2==0) and (d%2==0)):
         return c,d
    elif((a%2==0) and (b%2==0) and (c%2!=0) and (d%2!=0)):
         return a,b
    elif((a%2!=0) and (b%2==0) and (c%2!=0) and (d%2==0)):
        return b,d
    elif((a%2!=0) and (b%2==0) and (c%2==0) and (d%2!=0)):
        return b,c
    elif((a%2==0) and (b%2!=0) and (c%2!=0) and (d%2==0)):
        return a,d
    elif((a%2==0) and (b%2!=0) and (c%2==0) and (d%2!=0)):
        return a,c
    elif((a%2==0) and (b%2!=0) and (c%2!=0) and (d%2!=0)):
        return a
    elif((a%2!=0) and (b%2==0) and (c%2!=0) and (d%2!=0)):
        return b
    elif((a%2!=0) and (b%2!=0) and (c%2==0) and (d%2!=0)):
        return c
    else:
        return d
    return len(filtra_pares)