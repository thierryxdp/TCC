def pontos_por_time(n):
    I = n[0]     # Jogo 1 (J1)
    V = n[1]     # Jogo 2 (J2)
    T1 = I[0]    # Time 1 (T1)
    T2 = I[1]    # Time 2 (T2)
    M = I[2]     # Placar J1
    N = V[2]     # Placar J2
    X = M[0]     # Gols T1 em J1
    Y = M[1]     # Gols T2 em J1
    Z = N[0]     # Gols T2 em J2
    W = N[1]     # Gols T1 em J2
    P = 0        # Pontos T1
    Q = 0        # Pontos T2    
    if X > Y:
        P += 3
    if X < Y:
        Q += 3
    if X == Y:
        P += 1 ; Q += 1
    if Z > W:
        Q += 3
    if Z < W:
        P += 3
    if Z == W:
        P += 1 ; Q += 1
	if P > Q:
        return {T1:P,T2:Q}
    else:
        return {T2:Q,T1:P}