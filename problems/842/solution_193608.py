def pontos_por_time(n):
    """Dada a lista n, retorna o nome dos times e os pontos
    conquistados nos jogos"""
    I = n[0] # Jogo da ida
    V = n[1] # Jogo da volta
    M = A[2] # Placar do jogo da ida
    N = B[2] # Placar do jogo da volta
    X = M[0] # Gols do Cormengo em I
    Y = M[1] # Gols do Flaminthians em I
    Z = N[0] # Gols do Flaminthians em V
    W = N[1] # Gols do Cromengo em V