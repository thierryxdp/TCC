def bolo(A, B, C):
    '''função que recebe a quantidade de ingredientes e retorna quantos
    bolos é possivel fazer'''
    return min(A//2, B//3, C//5)