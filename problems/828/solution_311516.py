def primo(n):
    """Pede um número inteiro e verifica se ele é primo,
    retornando True ou False.
    int->bool"""
    import math
    from math import sqrt, ceil
    #Para n<=3
    if n<2:
        return False
    if n==2 or n==3:
        return True
    #Filtrando pares>2 e múltiplos de 3
    if n%2 ==0 or n%3 == 0:
        return False
    #Agora usando o critério x=6k-1 e x+2=6k+1
    #para n>=5
    #e lembrando que não é preciso testar para divisores
    #maiores que sqrt(n). Por exemplo: para n=36, a lista
    #de divisores é [2,3,4,6,9,12,36]. Mas 4*9=36 e 9*6=36,
    #ou seja, não é necessário testar para divisores>sqrt(36)
    for x in range(5,ceil(sqrt(n))+1,6):
        if x**2<=n:
            if n%x == 0 or n%(x+2) == 0:
                return False
    return True