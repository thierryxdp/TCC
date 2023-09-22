def retira_pontuacao(frase):
    "Substitui todas as pontuações de uma frase por espaço "
    frase=frase.replace('...','')
    frase=frase.replace('-',' ')
    frase=frase.replace('!','')
    frase=frase.replace('?','') 
    frase=frase.replace(',','')
    frase=frase.replace(';','')
    frase=frase.replace(':','')
    frase=frase.replace(".",'')
    frase=frase.replace("[",'')
    frase=frase.replace("]",'')
    return frase

def inverte(frase):    
    "Inverte a ordem das palavras de uma frase"
    frase= str.lower(retira_pontuacao(frase))
    frase=list(reversed(frase.split(' ')))
    return ' '.join(frase)