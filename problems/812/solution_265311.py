def retira_pontuacao(texto):
    """Retorna o texto original sem pontuacoes e com um espaço no lugar
    dado um texto com pontuacoes
    assinatura: str-->str
    testes: retira_pontuacao('e,e.e;e:e!e?e')== 'e e e e e e e'
    """
    a = str.replace(texto, ('-'), ' ')
    b = str.replace(a, (','), ' ')
    c = str.replace(b, (':'), ' ')
    d = str.replace(c, (';'), ' ')
    e = str.replace(d, ('.'), ' ')
    f = str.replace(e, ('!'), ' ')
    g = str.replace(f, ('?'), ' ')
    return g