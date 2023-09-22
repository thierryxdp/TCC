def soma_h(n):
    '''Calcula e retorna o valor de H.
int->float'''
    H=0
    for x in range(1,n+1):
        if x<n+1:
            H+=(1/x)
    return round(H,2)