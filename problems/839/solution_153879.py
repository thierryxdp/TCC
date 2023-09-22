#2
def carros(pessoas:int,capacidade:int)->int:
    '''caso o número seja quebrado o +0.999999 e o //1 vai arredondar para o número inteiro acima'''
    return (pessoas/capacidade+0.9999999999999)//1