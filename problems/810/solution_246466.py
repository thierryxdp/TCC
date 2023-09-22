def retira_pontuacao(frase):
    frase=frase.replace('.',' ').replace(',',' ').replace(':',' ').replace('!',' ').replace('-',' ').replace('?',' ').replace(';',' ')
    return frase

def inverte(frase):
    
    frase=str.upper(frase)
    frase={retira_pontuacao(frase)}
    list(dict.items(frase))
    list.reverse(frase)
   
    return frase