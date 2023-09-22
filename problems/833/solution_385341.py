def conta_numero(num,mat):
    '''função responsável por receber um número, num, e uma matriz,mat, e dizer quantas vezes o número aparece nesta matriz'''
    total=0
    for i in mat:
        for j in i:
            if num==j:
                total=total+1
    return total