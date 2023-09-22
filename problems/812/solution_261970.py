def retira_pontuacao(frase):
    ''' '''
    pontuacao= '!',':',';','?','...',',','-','.'
    return str.strip(frase, pontuacao)