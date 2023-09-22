def retira_pontuacao(frase):
    ''' '''
    pontuacao= '!',':',';','?','...',',','-','.'
    return replace(frase, pontuacao,' ')