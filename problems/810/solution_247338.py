def retira_pontuacao(text):
    '''Retorna o dado texto sem suas pontuações
    srt -> str'''
    return text.replace('...', ' ').replace('.', ' ').replace('-', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ').replace(',', ' ')

def inverte(text):
    '''Retorna o dado texto intertendo, sem letras maiúsculas e sem pontuações
    srt -> srt'''
    lista_do_texto = retira_pontuacao(text).lower().replace('  ', ' ').strip().split(' ')
    lista_do_texto.reverse()
    return str.join(' ', lista_do_texto)