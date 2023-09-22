def retira_pontuacao(frase):
  """essa funçao recebe uma frase de entrad e susbtitui os caracteres de pontuaçao da frase por espaços;
 string ->string"""
frase = frase.replace('!',' ')
frase = frase.replace('?',' ')
frase = frase.replace(',',' ')
frase = frase.replace('.',' ')
frase = frase.replace('-',' ')
frase = frase.replace(':',' ')
frase = frase.replace(';',' ')
 return frase