def media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia, a função vai 
    retornar a média de todos os números da matriz com 2 casas
    decimais de precisão.
       A matriz deve ser escrita entre colchetes[], com cada linha
    da matriz sendo representada dentro de um colchetes também;
       matriz (lista de listas) --> float"""
    numeros = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(numeros, matriz[i][j])
            qtd_numeros = len(numeros)
            somaDosNum = sum(numeros)
    return round((somaDosNum / qtd_numeros),2)