def carros(p,c):
    '''calcula a quantidade de carros de capacidade c necessária para transportar p pessoas'''
    if p=0:
        return 0
    else:
        return p//c+1