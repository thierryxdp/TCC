def soma_h(n):
    '''Calcula e retorna o valor de H.
H=1+1/2+1/3...1/n.
int->float'''
    H=0
    for i in range(1,n+1):
        if i<n+1:
            H+=(1/i)
    return round(H,2)