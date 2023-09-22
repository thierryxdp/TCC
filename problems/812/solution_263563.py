def retira_pontuacao(texto):
    return (texto.replace('-',' ')
    texto.replace(',',' ')
    texto.replace(':',' ')
    texto.replace(';',' ')
    texto.replace('.',' ')
    texto.replace('...',' ')
    texto.replace('!',' ')
    texto.replace('?',' '))