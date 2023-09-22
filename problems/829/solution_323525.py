def soma_h(N):
    '''função que calcula o valor de H, com N termos, onde N é inteiro e dado como entrada.O resultado é retornado, somente, com 2 casas deciamis; int -> int'''
    H=0
    for k in range(1,N+1):
        H+=(1/k)
    return round(H,2)