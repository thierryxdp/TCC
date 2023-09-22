def media_matriz(matriz):
    """Função que dada uma matriz de números inteiros calcula a média
       de todos os números da matriz.
       
       Parameters:
       matriz: Matriz que será analisada pela função
       
       Returns:
       Retorna a média dos números que fazem parte da matriz.
       list -> float"""
    elementos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz1 = list.append(elementos, matriz[i][j])
    return round(sum(elementos)/elementos, 2)