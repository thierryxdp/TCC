def qtd_divisores(n):
    '''recebe numero inteiro e retorna a quantidade de 
    divisores que o numero possui.
    entrada: int
    saida: int'''
    D=[]
    for N in range(1,n+1):
        if n % N == 0:
            list.append(D,N)
    return len(D)