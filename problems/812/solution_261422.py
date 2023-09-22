def retira_pontuacao(texto):
    """Função que retorna a frase onde todoso os caracteres de pontuação são substituídos por espaço"""
    x = '...'
    y = '-'
    z = '.'
    w = ';'
    r = ''
    j = ':'
    k = ','
    l = '!'
    b = ' '
    i = str.replace(texto, x,b)
    o = str.replace(i, y,b)
    u = str.replace(o, z,b)
    n = str.replace(u, w,b)
    m = str.replace(n, r,b)
    p = str.replace(m, j,b)
    q = str.replace(p, k,b)
    r = str.replace(q, l,b)
    texto=r
    return texto