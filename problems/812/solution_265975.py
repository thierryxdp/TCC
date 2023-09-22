def retira_pontuacao(frase):
    """retorna uma frase onde toda a pontuacao é
    substituida por espaço.
    str -> str"""
    travessao = frase.split('-')
    a = ' '.join(travessao)
    virgula = a.split(',')
    b = ' '.join(virgula)
    dois_pontos = b.split(':')
    c = ' '.join(dois_pontos)
    ponto_virgula = c.split(';')
    d = ' '.join(ponto_virgula)
    ponto_final = d.split('.')
    e = ' '.join(ponto_final)
    exclamacao = e.split('!')
    f = ' '.join(exclamacao)
    interrogacao = f.split('?')
    g = ' '.join(interrogacao)
    return g