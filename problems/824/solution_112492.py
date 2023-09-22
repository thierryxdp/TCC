def uppCons (frase):
    """Retorna uma frase com todas as consoantes da frase dada como entrada
    em letra maiúscula. str-> str"""
    i = 0
    uppercons = []
    while i < len(frase):
        if frase[i] in ['b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, y, w, z B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, X, Y, W, Z']:
            uppercons = uppercons + [str.upper(frase[i]),]
        else:
            uppercons = uppercons + [frase[i],]
    i = i+1
    return uppercons