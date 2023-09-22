def carros(p,c):
    '''função que calcula a quantidade de carros necessária para transportar p pessoas, tendo cada carro uma capacidade c; int,int-->int'''
    if p<c:
        return 1
    else:
        return p//c+1