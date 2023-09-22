def bolos(a,b,c):
    '''funcao que dada a quantidade de farinha de trigo, ovos
    e leite, calcula quantos bolos podem ser feitos a partir da 
    quantidade de ingredientes que voce possui'''
    return min(a//2,b//3,c//5)