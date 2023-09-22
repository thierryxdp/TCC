def melhor_volta(matriz):
    """Função que dada uma matriz de corredores e voltas, retorna o resultado da corrida."""
    """List -> Tuple"""
    lista = []
    melhor_volta = min(lista)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista.append(matriz[i][j])
    return matriz.index(melhor_volta)