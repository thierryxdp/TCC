def retira_pontuacao(texto):
    """Recebe uma texto contido em uma string e retorna o mesmo texto subistituindo as pontuações por espaços vazios
    testes: retira_pontuacao('a. b!') == 'a b'
    retira pontuacao('a... b: c; d, e? f-') == 'a b c d e f'
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

def inverte(texto):
    """Recebe um texto contido em uma string, e o retorna sem pontuação e com a ordem das palavras trocadas
    testes inverte('a. b! c;') == 'c b a'
    inverte('1. 2... 3') == '3 2 1'
    assinatura: str --> str
    """
    x = str.split(retira_pontos(texto))
    y = x[::-1]
    return str.join(' ', y)