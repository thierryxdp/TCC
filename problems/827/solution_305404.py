#Entrada: um numero inteiro
#1-Precisamos saber quais os divisores exatos do numero
#2-Ao saber quais são, contar quantos são 
#3-Retornar a quantidade
def qtd_divisores(n:int) -> int:
    """Conta a quantidade de divisores exatos de um 
    numero"""
    quantDivisores=0
    for numero in range(1,n+1):
        if n%numero==0:
            quantDivisores+=1
    return quantDivisores