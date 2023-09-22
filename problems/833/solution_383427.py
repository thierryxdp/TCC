def conta_numero(n,M):
    """Recebe um número inteiro e uma matriz M de inteiros
       de tamanho qualquer e retorna quantas vezes aquele número 
       aparece na matriz
       parâmetros de entrada:int,list(list)
       parâmetros de saída:int"""
    M=[]
    for i in range(len(M)):
        for j in range(len(M[0])):
            return list.count(M,n)