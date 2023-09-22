def retira_pontuacao (frase):
""" Função que retira todas as pontuações especificadas de uma string"""
     nf = ''
     nf = frase.replace (',', ' ').replace (';', ' ').replace ('!', ' ').replace ('-', ' ').replace ('.', ' ').replace ('?', ' ')
     return nf