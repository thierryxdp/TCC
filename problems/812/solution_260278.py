def retira_pontuacao(texto):
    ''' substitui as pontuacoes por espaços.
        str-->str'''
    return texto.replace('.',' ') + texto.replace('-',' ') + texto.replace('!',' ')+ texto.replace('?',' ') + texto.replace('...',' ') + texto.replace(':',' ') + texto.replace(';',' ')+ texto.replace(';',' ')