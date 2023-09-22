def retira_pontuacao (frase):
     nf = ''
     nf = frase.replace (',', ' ').replace (';', ' ').replace ('!', ' ').replace ('-', ' ').replace ('.', ' ').replace ('?', ' ')
     return nf