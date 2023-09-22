#Start your python function here
def filtra_pares(a,b,c,d):
    """função que recebe uma tupla com quatro numeros inteiros e retorne uma nova tupla que tem elementos pares respectivamente; tuple,tuple,tuple,tuple-> int"""
    lista1=[a,b,c,d]
    lista2=(lista1%2==0)
    return lista2