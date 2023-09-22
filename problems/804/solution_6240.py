#Start your python function here
def filtra_pares(a,b,c,d):
    """função que recebe uma tupla com quatro numeros inteiros e retorne uma nova tupla que tem elementos pares respectivamente; int,int,int,int -> tuple"""
    tupla=(a,b,c,d)
    if (int(len(tupla)%2==0)):
        return int(tupla)