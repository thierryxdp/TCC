def retira_pontuacao(texto):
    return texto.replace('.',' ') and texto.replace(',',' ') and texto.replace('-',' ') and texto.replace(':',' ') and texto.replace(';',' ')