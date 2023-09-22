#Start your python function here
def filtra_pares(a,b,c,d):
    """função que recebe uma tupla com quatro numeros inteiros e retorne uma nova tupla que tem elementos pares respectivamente; int,int,int,int -> tuple"""
    tupla1=a
    tupla2=b
    tupla3=c
    tupla4=d
    tupla=tupla1,tupla2,tupla3,tupla4
    if (int(len(tupla)%2==0)):
        return int(tupla)