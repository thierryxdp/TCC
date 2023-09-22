#def retira_pontuacao(frase):
 #   s1 = frase.replace('.', ' ')
  #  s2 = s1.replace('...', ' ')
   # s3 = s2.replace('!', ' ')
   # s4 = s3.replace('?', ' ')
   # s5 = s4.replace('-', ' ')
   # s6 = s5.replace(';', ' ')
   # s7 = s6.replace(':', ' ')
   # return print(s7)
def retira_pontuacao(frase):
    pontos = '.' or '...' or ';' or '?' or ':' or '!' or '-'
    if pontos in frase:
        n_frase = frase.replace(pontos, ' ')
        return print(n_frase)
    else:
        return print(frase)