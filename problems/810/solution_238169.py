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
     lista = str.split(retira_pontuacao(texto))
     inverso = ' '.join (lista[::-1])
     inverso = str.lower(inverso)
     return inverso