from math import sqrt
from math import floor
def primo(numero):
    '''funcao que recebe como entrada um numero inteiro positivo e verifica se esse numero e primo ou nao, retornando um valor booleano
    int -> bool'''
    contador=0
    for i in range(2,floor(sqrt(numero))+1):
        if numero%i==0:
            contador+=1
    if contador==0:
        return False