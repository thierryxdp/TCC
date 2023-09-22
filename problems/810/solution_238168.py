def retira_pontuacao (frase):
     '''Retira a pontuação de uma frase;
     str -> str'''
     texto = frase.replace('.',' ')
     texto = texto.replace(';',' ')
     texto = texto.replace(',',' ')
     texto = texto.replace(':',' ')
     texto = texto.replace('!',' ')
     texto = texto.replace('?',' ')
     texto = texto.replace('-',' ')         
     return texto
    
def inverte (texto):
     '''Inverte as palavras de uma frase e retira sua pontuação;
     str -> str'''
     lista = str.split(texto)
     inverso = ' '.join (lista[::-1])
     inverso = retira_pontuacao(inverso)
     return inverso