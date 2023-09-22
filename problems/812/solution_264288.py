def retira_pontuacao(frase):
    ''' Função que retorna uma frase com sua pontuação substiuída por espaços
    incluindo a pontuação de encerramento da frase.   str=> str'''
    frase = x
    if '—' in x:
        x.replace('—', '')
    if ',' in x:
        x.replace(',', '')
    if ':' in x:
        x.replace(':', '')
    if ';' in x:
        x.replace(';', '')
    if '.' in x:
        x.replace('.', '')    
    if '?' in x:
        x.replace('?', '')
    if '!' in x:
        x.replace('!', '')
    return x