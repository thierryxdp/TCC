def retira_pontuacao(texto):
    return str.replace(texto,'.',' ') + texto.replace(',',' ')  texto.replace('-',' ') and texto.replace(':',' ') and texto.replace(';',' ')