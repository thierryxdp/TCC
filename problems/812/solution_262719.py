def retira_pontuacao (frase):
     x = ''
     x = frase.replace (',', ' ').replace (';', ' ').replace ('!', ' ').replace ('-', ' ').replace ('.', ' ').replace ('?', ' ')
     return x