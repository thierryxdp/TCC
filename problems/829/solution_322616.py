def soma_h(N):
    '''Recebe um termo N e retorna o valor de H com N termos..
    int-> float'''
    i=1
    h=0
    while i<=N:
        h=h+1/i
        i=i+1
    return h