from math import *
def soma_h(N):
    """função que calcula e retorna o vbalor de H com N termos onde N é inteiro
    e dado como entrada"""
    H=0
    for termo in range(1,N+1):
        H=H+1/termo
    return round(H,2)