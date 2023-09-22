def pontos_por_time(n):
    """Dada a lista n, retorna o nome dos times e os pontos
    conquistados nos jogos"""
    I = n[0]   # Jogo da ida
    V = n[1]   # Jogo da volta
    T1 = I[0]  # Definindo o primeiro time
    T2 = I[1]  # Definindo o segundo time
    M = I[2]   # Placar do jogo da ida
    N = V[2]   # Placar do jogo da volta
    X = M[0]   # Gols do T1 em I
    Y = M[1]   # Gols do T2 em I
    Z = N[0]   # Gols do T2 em V
    W = N[1]   # Gols do T1 em V
    p = (0,)     # Pontos do T1
    q = (0,)     # Pontos do T2
    P = p[0] 
    Q = q[0]
    if X > Y:
    	p + (3,)
    if X < Y:
    	q + (3,)
    if X == Y:
    	(p + (1,)) and (q + (1,))
    if Z > W:
        q + (3,)
    if Z < W:
        p + (3,)
    if Z == W:
        (p + (1,)) and (q + (1,))
    return {T1:P,T2:Q}