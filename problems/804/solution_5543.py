#Start your python function here
"""Dada a tupla de entrada com 4 números inteiros, retorna com uma nova
tupla contendo apenas os número pares dados.
tuple -> tuple"""
def filtra_pares(numeros):
    tupla= ()
    if (numeros[0]%2==0):
        return tupla + (numeros[0],)
    elif (numeros[1]%2==0):
        return tupla + (numeros[1],)
    elif (numeros[2]%2==0):
        return tupla + (numeros[2],)
    elif (numeros[3]%2==0):
        return tupla + (numeros[3],)
    else:
        return tupla