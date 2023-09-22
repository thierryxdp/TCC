def melhor_volta(matriz):
    """Função que dada uma matriz de corredores e voltas, retorna o resultado da corrida."""
    """List -> Tuple"""
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista.append(matriz[i][j])
        melhor_volta = min(lista)
    return (i,j,melhor_volta)