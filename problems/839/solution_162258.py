def carros(p,c=5):
    """calcula e retorna o número de carros de capacidade 'c' necessários para levar um número 'p' de pessoas em uma viagem
	entrada: int
	saída: int"""
    if (p<5 and p>0):
        return 1
    elif (p==0):
        return 0
    elif (p%c=0):
        return p//c
    else:
        return p//c+1