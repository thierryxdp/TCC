def retira_pontuacao(frase):
    ''' '''
    pontuacao= '!',':',';','?','...',',','-','.'
    return str.strip(frase,('!' and ':' and';'and'?'and'...'and','and'-'and'.'))