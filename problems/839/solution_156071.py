def carros(p,c=4):
    '''função que calcula quantos carros sao necessarios pra viagem.(entrada p -> int, entrada c quando necessario -> intww)'''
    if p<=5:
        return 1
    if c<4 or c>4 and p<c:
        return 1
    return p/c