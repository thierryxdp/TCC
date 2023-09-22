def retira_pontuacao(texto):
    '''função que retira pontuação do texto'''
    return texto.replace('!',' ')and texto.replace('?',' ') and texto.replace('.',' ')