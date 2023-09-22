def retira_pontuacao (frase):
     '''Retira a pontuação de uma frase;
     str -> str'''
     texto = frase.replace('.',' ')
     texto = texto.replace(';',' ')
     texto = texto.replace(',',' ')
     texto = texto.replace(':',' ')
     texto = texto.replace('!',' ')
     texto = texto.replace('?',' ')
              
     return texto