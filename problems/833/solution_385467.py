def conta_numero(num,mat):
    '''dado um numero inteiro retorn quantas vezes aquele numero aparece na raiz
    int->int'''
    total=0
    for i in mat:
        for j in i:
            if num==j:
                total=total+1
    return total