def uppCons(frase):
    """Funcao que recebe uma frase e retorna a mesma frase so que com as consoantes maiusculas. str=>str"""
    frase1=''
    x=0
    while x<len(frase):
        if frase[x] in "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, y, w, z":
            frase1= frase1=str.upper(frase[x])
        else:
            frase1= frase1+frase1[x]
        x=x+1
    return frase1