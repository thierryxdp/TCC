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
    ocorrencias=0
    for linha in matriz:
        if numero in linha:
            k=list.count([matriz], linha)
        ocorrencias = ocorrencias +1
    return k