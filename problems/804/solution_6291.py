#Start your python function here
def filtra_pares(tupla):
    """função que recebe uma tupla com quatro numeros inteiros e retorne uma nova tupla que tem elementos pares respectivamente; int,int,int,int -> tuple"""
    tVazia=()
    if (tupla[0]%2==0):
        tVazia= tVazia + (tupla[0],)
    if (tupla[1]%2==0):
        tVazia= tVazia + (tupla[1],)
    if (tupla[2]%2==0):
        tVazia= tVazia + (tupla[2],)
    if (tupla[3]%2==0):
        tVazia= tVazia + (tupla[3],)
    return tVazia