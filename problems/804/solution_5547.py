#Start your python function here
"""Dada a tupla de entrada com 4 números inteiros, retorna com uma nova
tupla contendo apenas os número pares dados.
tuple -> tuple"""
def filtra_pares(numeros):
    tupla= ()
    if (abs(numeros[0])%2==0):
    	tupla = tupla + (numeros[0],)
    elif (abs(numeros[1])%2==0):
        tupla = tupla + (numeros[1],)
    elif (abs(numeros[2])%2==0):
        tupla = tupla + (numeros[2],)
    elif (abs(numeros[3])%2==0):
        tupla = tupla + (numeros[3],)
        
        return tupla