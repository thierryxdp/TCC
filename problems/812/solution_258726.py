def retira_pontuacao(frase):
    
    x='!'or'?'or'.'or'...' or ',' or ':' or ';'
    
    return str.strip(frase,x)