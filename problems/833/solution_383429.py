def conta_numero(n,M):
    """Recebe um número inteiro e uma matriz M de inteiros
       de tamanho qualquer e retorna quantas vezes aquele número 
       aparece na matriz
       parâmetros de entrada:int,list(list)
       parâmetros de saída:int"""
    numero=0
    M=[]
    total=0
    for i in range(len(M)):
        for jin range(len(M[0])):
            numero=list.count(M,n)
    total=sum(list.count(M,n))
    return M