def retira_pontos(texto):
    """Recebe uma texto contido em uma string e retorna o mesmo texto subistituindo as pontuações por espaços vazios
    testes: retira_pontos('a. b!') == 'a b'
    retira pontos('a... b: c; d, e? f-') == 'a b c d e f'
    assinatura: str --> str
    """
    a = texto.replace('.', ' ')
    b = a.replace('-', ' ')
    c = b.replace(',', ' ')
    d = c.replace(':', ' ')
    e = d.replace(';', ' ')
    f = e.replace('!', ' ')
    g = f.replace('?', ' ')
    return g