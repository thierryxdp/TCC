def retira_pontuacao(frase):
    
    x='!'and'?'and'.'and'...' and ',' and ':' and ';'
    
    return str.strip(frase,x)