def retira_pontuacao(frase):
    
    x=['!','?',',',':',';']
    
    return str.strip(frase,'!','?',',',':',';')