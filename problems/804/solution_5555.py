#Start your python function here
"""Dada a tupla de entrada com 4 números inteiros, retorna com uma nova
tupla contendo apenas os número pares dados.
tuple -> tuple"""
def filtra_pares(numeros):
    pares= ()
    if(abs(numeros[0])%2==0):
    	pares += (numeros[0],)
    if(abs(numeros[1])%2==0):
        pares += (numeros[1],)
    if(abs(numeros[2])%2==0):
        pares += (numeros[2],)
    if(abs(numeros[3])%2==0):
        pares += (numeros[3],)
        
    return pares