def conta_numero(numero,matriz):
    """Cálculo de uma função que dado um número intero e uma matriz de inteiros, de qualquer tamanho,
    conta e retorna quantas vezes aquele número aparece na matriz.
    
       Parameters: 
       numero: número a ser procurado na matriz
       matriz: matriz onde ocorrerá a busca
       
       Returns:
       Retorna quantas vezes aquele número aparece na matriz, dado que:
       int, list -> int
    """
    m= len(matriz)
    n= len(matriz[0])
    ocorrencias=0
    p=0
    for i in range(m):
        for j in range(n):
            if p(numero,matriz,i,j):
                ocorrencias += 1
            if p(numero, matriz, i, j):
                ocorrencias += 1
    return ocorrencias