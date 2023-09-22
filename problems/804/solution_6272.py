#Start your python function here
def filtra_pares(tupla):
    """função que recebe uma tupla com quatro numeros inteiros e retorne uma nova tupla que tem elementos pares respectivamente; int,int,int,int -> tuple"""
    a= tupla[0]
    b= tupla[1]
    c= tupla[2]
    d= tupla[3]
    if (len(tupla)%2==0):
        return tupla%2==0