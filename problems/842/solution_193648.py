def pontos_por_time(n):
    I = n[0]
    V = n[1]
    T1 = I[0]
    T2 = I[1]
    M = I[2]
    N = V[2]
    X = M[0]
    Y = M[1]
    Z = N[0]
    W = N[1]
    p = ()
    q = ()
    P = p[0]
    Q = p[0]
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