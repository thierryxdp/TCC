def retira_pontuacao(frase):
    
    frase2=frase
    str.split(frase,'.')
    str.split(frase,'?')
    str.split(frase,'!')
    str.split(frase,'...')
    
    return len(frase2)