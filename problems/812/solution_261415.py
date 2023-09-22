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
    i = str.replace(texto, x, ' ')
    o = str.replace(i, y, ' ')
    u = str.replace(o, z, ' ')
    n = str.replace(u, w, ' ')
    m = str.replace(n, r, ' ')
    p = str.replace(m, j, ' ')
    q = str.replace(p, k, ' ')
    r = str.replace(q, l, ' ')
    texto = r
    return texto