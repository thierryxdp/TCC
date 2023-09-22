def retira_pontuacao(s):
    pontuacao='!'or'.'or','or';'or'-'or'/'or':'
    
    return str.join("",str.split(s,pontuacao))