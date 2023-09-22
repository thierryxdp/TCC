def soma_h(N):
    """A função recebe um número 'N' como inteiro"""
    H=1
    i=0
    for num in range(1,N+1):
        lista=list(range(1,N+1))
        H= H * lista[i]
        i=i+1
    return round(H,2)