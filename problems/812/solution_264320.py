def retira_pontuacao(frase):
    ''' Função que retorna uma frase com sua pontuação substiuída por espaços
    incluindo a pontuação de encerramento da frase.   str=> str'''
    if '.' or '?'or '!'or ':'or ';'or '—' or ',' in frase:
        return frase.replace('.', ' ').replace('?',' ').replace('!',' ').replace(':',' ').replace(';',' ').replace('—',' ')