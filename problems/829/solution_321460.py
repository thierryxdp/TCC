def soma_h(N):
    """ Função que calcula e retorna o valor de H com N; int-> float"""
    H=0
    for i in range(1,N+1):
        H= H+1/i
    return H