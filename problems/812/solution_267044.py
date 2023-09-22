def retira_pontuacao(frase):
    """A função recebe uma frase e substitui todos os caracteres de pontuação por espaço.
    string -> string"""
    e1 = frase.replace('–', ' ')
    e2 = e1.replace(',', ' ')
    e3 = e2.replace(':', ' ')
    e4 = e3.replace(';', ' ')
    e5 = e4.replace('.', ' ')
    e6 = e5.replace('!', ' ')
    e7 = e6.replace('?', ' ')
    e8 = e7.replace('...', ' ')
    e9 = e8.replace('-', ' ')
    return e9