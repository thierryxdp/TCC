def fatorial (n):
    '''calcula a fatorial do valor n
int->int'''
    i=1
    j=int(n)
    while i<j:
        n=int(n)*(j-1)
        j=j-1
    return int(n)