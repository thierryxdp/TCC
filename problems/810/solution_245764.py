def retira_pontuacao (frase):
     nf = ''
     nf = frase.replace (',', ' ').replace (';', ' ').replace ('!', ' ').replace ('-', ' ').replace ('.', ' ').replace ('?', ' ')
     return nf

    
def inverte (frase):
    frase = str.split(frase)
    list.reverse(frase)
    
    return str.lower(retira_pontuacao(' '.join (frase)))