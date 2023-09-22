def retira_pontuacao(frase):
    ''' '''
    pontuacao= '!',':',';','?','...',',','-','.'
    return str.replace(frase, pontuacao,' ')