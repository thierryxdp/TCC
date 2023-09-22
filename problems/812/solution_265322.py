def retira_pontuacao(frase):
    """Função que retorna a frase sem pontuação"""
    x = str.replace(frase, ',',' ')
    y = str.replace(x, ',',' ')
    z = str.replace(y, ':',' ')
    a = str.replace(z, ';',' ')
    b = str.replace(a, '!',' ')
    c = str.replace(b, '?',' ')
    d = str.replace(c, '-',' ')
    return d