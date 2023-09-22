def retira_pontuacao(frase):
    
    pontuacao=['\.|\!|\?|\.\.\.']
    
    return str.split(frase,pontuacao)