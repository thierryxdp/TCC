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

  #Retira a pontuação da frase
  frase_pontos = retira_pontuacao(frase)

  #Separa cada palavra da frase
  frase_dividida = frase_pontos.split()

  #Inverte a lista (ordem das palavras)
  list.reverse(frase_dividida)

  #Transforma a lista em string, com letras minúsculas
  frase_final = ' '.join(frase_dividida).lower()
  return frase_final