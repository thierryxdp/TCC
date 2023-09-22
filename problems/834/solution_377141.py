def media_matriz(matriz):
    """Função que dada uma matriz de números inteiros calcula a média
       de todos os números da matriz.
       
       Parameters:
       matriz: Matriz que será analisada pela função
       
       Returns:
       Retorna a média dos números que fazem parte da matriz.
       list -> float"""
    elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elementos = elementos + 1
    return round(sum(elementos)/elementos, 2)