def soma_h(n):
    '''essa função faz soma das frações '1/n' aredondando até a segunda casa decimal.
    int -> float'''
    a=list(range(1,n+1))
    h=0
    for x in a:
        h+=1/x
    return round(h,2)