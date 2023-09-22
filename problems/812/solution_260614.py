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