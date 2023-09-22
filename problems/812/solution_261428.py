def retira_pontuacao(texto):
    """Função que retorna a frase onde todos os caracteres de pontuação são substituídos por espaço"""
    """str-->str"""
    i = str.replace(texto, '...',' ')
    o = str.replace(i, '-',' ')
    u = str.replace(o, '.',' ')
    n = str.replace(u, ';',' ')
    m = str.replace(n, '?',' ')
    p = str.replace(m, ':',' ')
    q = str.replace(p, ',',' ')
    r = str.replace(q, '!',' ')
    texto=r
    return texto