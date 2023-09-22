def retira_pontuacao(frase):
   '''Função que, dada uma frase, retorna a frase onde todos os caracteres de pontuação (incluindo travessão, vírgula, dois pontos, ponto e vírgula, além da pontuação de encerramento de frase) tenham sido substituídos por espaço
   str -> str'''

   frase = frase.split('-')
   frase = ' '.join(frase)
   frase = frase.split(',')
   frase = ' '.join(frase)
   frase = frase.split(':')
   frase = ' '.join(frase)
   frase = frase.split(';')
   frase = ' '.join(frase)
   frase = frase.split('!')
   frase = ' '.join(frase)
   frase = frase.split('?')
   frase = ' '.join(frase)
   frase = frase.split('.')
   frase = ' '.join(frase)
   frase = frase.split('...')
   frase = ' '.join(frase)
   
   return frase

def inverte(frase):
  '''Função que, dada uma frase, retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.
  str -> str'''

  frase_invertida = list.reverse(frase)
  frase_invertida = retira_pontuacao(frase_invertida)

  return frase_invertida.lower()