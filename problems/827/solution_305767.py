#Quero uma função que calcule quantos divisores um número n tem
#Resolução:
#1.Criar um laço para divisores
#2.Verificar se n é divisível pelos divisores do laço
#acrescentar +1 na soma caso seja divisível


def qtd_divisores(n:int)->int:
    """funcao que conta a quatidade de divisores
    de um número n dado como entrada"""
    
    soma=0
    for divisores in range(1,n+1):
        if n%divisores==0:
            soma=soma+1
            
    return soma