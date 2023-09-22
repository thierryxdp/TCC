def conta_numero(n,M):
    """Recebe um número inteiro e uma matriz M de inteiros
       de tamanho qualquer e retorna quantas vezes aquele número 
       aparece na matriz
       parâmetros de entrada:int,list(list)
       parâmetros de saída:int"""
    numero=0
    M=[]
    total=0
    for linha in M:
        for aij in linha:
            if aij==n:
                numero=numero+1
                total=total+numero
    return total