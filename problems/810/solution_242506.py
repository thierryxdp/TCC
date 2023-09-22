def retira_pontuacao(texto):
    '''Recebe um texto e retorna ele sem pontuações
       str -> str'''
    texto = texto.replace('...', ' ')
    texto = texto.replace('!', ' ')
    texto = texto.replace('?', ' ')
    texto = texto.replace('.', ' ')
    texto = texto.replace('-', ' ')
    texto = texto.replace(':', ' ')
    texto = texto.replace(',', ' ')
    texto = texto.replace(';', ' ')
    return texto

def inverte(texto):
    '''Retorna texto com a ordem das palavras invertidas
       str -> str'''
    texto = retira_pontuacao(texto)
    texto = texto.split(' ')[::-1]
    texto = str.join(' ', texto)
    return texto