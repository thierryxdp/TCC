def retira_pontuacao (frase):
     nf = ''
     nf = frase.replace (',', '').replace (';', '').replace ('!', '').replace ('-', ' ').replace ('.', '').replace ('?', '')
     return nf

    
def inverte (frase):
    x = retira_pontuacao(frase)
    frase = str.split(frase)
    x = str.split(x)
    list.reverse(x)
    x = str.lower(' '.join(x))
    return x