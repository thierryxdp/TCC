def uppCons(frase):
    """Retorna a frase dada com todas as suas consoantes em maiuscula;
       Entrada: str;
       Saida: str
    """
    consoantes = [b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, z]
    for consoantes in frase:
        frase = consoantes.upper()
    return frase