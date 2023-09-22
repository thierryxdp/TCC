def melhor_volta (matriz):
    """funçao que recebe uma matriz 6x10 que representa o tempo e voltas de cada corredor em uma corrida e retorna quem fez em menor tempo, o tempo e em qual volta;
    entrada: list;
    saida: tuple (int,int,int)."""
    
    menor = min(matriz)
    for linha in matriz:
        for coluna in linha:
            if coluna == menor:
    return (linha, coluna, menor)