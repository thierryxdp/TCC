def retira_pontuacao(texto):
    a = str.replace(texto, ('-'), ' ')
    b = str.replace(a, (','), ' ')
    c = str.replace(b, (':'), ' ')
    d = str.replace(c, (';'), ' ')
    e = str.replace(d, ('.'), ' ')
    f = str.replace(e, ('!'), ' ')
    g = str.replace(f, ('?'), ' ')
    return g

def inverte(texto):

    """Retorna o texto com as palavras invertidas, sem pontuacao
    e com todas as letras minusculas dado um texto

    assinatura: str-->str

    Testes:
    inverte('A MEU DEUS DO CEU COMO. . . PODE UMA.COISA!!!!DESSAS')=='dessas coisa uma pode como ceu do deus meu a'"""
    
    i = str.lower(retira_pontuacao(texto))
    j = str.split(i)[::-1]

    k = str.join(' ',j)
    return k