def bolos(A,B,C):
    '''calcula a quantidade max de bolos dado os ingredientes A,B,C'''
    a=A//2
    b=B//3
    c=C//5
    return min(a,b,c)