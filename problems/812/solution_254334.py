def retira_pontuacao(frase):
    if str.count(frase,'!')>0:
        return frase.replace('!','')
    
    if str.count(frase, ',')>0:
        return frase.replace('!','')