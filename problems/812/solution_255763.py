def retira_pontuacao(frase):
    
    frase2 = ['!','?','.','-',',',':',';']
    
    return str.replace(frase,'!','?','.','-',',',':',';',' ')