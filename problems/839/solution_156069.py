def carros(p,c=5):
    '''função que calcula quantos carros sao necessarios pra viagem.(entrada p -> int, entrada c quando necessario -> intww)'''
    if p<=5:
        return 1
    if c<5 or c>5 and p<c:
        return 1
    return p/c