def retira_pontuacao(frase):
    ''' Função que retorna uma frase com sua pontuação substiuída por espaços
    incluindo a pontuação de encerramento da frase.   str=> str'''
    
    if '—' in texto:
        texto.replace('—', ' ')
    if ',' in texto:
        texto.replace(',', ' ')
    if ':' in texto:
        texto.replace(':', ' ')
    if ';' in texto:
        texto.replace(';', ' ')
    if '.' in texto:
        texto.replace('.', ' ')    
    if '?' in texto:
        texto.replace('?', ' ')
    if '!' in texto:
        texto.replace('!', ' ')
    return texto