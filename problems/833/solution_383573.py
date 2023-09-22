def conta_numero(numero,matriz):
    """Função que dado um número inteiro e uma matriz de inteiros de 
       tamanho qualquer, conta e retorna quantas vezes aquele número 
       aparece na matriz.
       int,list -> int
       
       Parâmetros: 
       numero: Número que será buscado e contada suas aparições na matriz
       matriz: Matriz de inteiros que será analisada pela função
       
       Returns: Quantas vezes aquele número aparece na matriz.
    """
    contagem = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                contagem += 1
    return contagem