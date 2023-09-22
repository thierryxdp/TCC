def media_matriz(matriz):
    """Cálculo de uma função que, dada uma matriz de inteiros não vazia, retorne 
    a média de todos os números desta matriz.
    
       Parameters:
       matriz: matriz que será dada como entrada e será calculada a média dos números desta
       
       Returns:
       Retorna a média de todos os números da matriz, dado que:
       list -> float
    """
    soma=0
    contagem=0
    for i in matriz:
        for v in i:
            soma= soma+v
            contagem=contagem+1
    return soma/contagem