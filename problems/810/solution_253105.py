def substitui(frase):
  '''Função que, ao receber uma frase(frase), substitui, nessa frase, toda pontuação por espaço 
  srt -> str'''
  frase=frase.replace(',',' ',frase.count(','))
  frase=frase.replace(':',' ',frase.count(':'))
  frase=frase.replace('?',' ',frase.count('?'))
  frase=frase.replace('-',' ',frase.count('-'))
  frase=frase.replace(';',' ',frase.count(';'))
  frase=frase.replace('!',' ',frase.count('!'))
  frase=frase.replace('...','.',frase.count('...'))
  frase=frase.replace('.',' ',frase.count('.'))
  return frase
def inverte(frase):
  '''Função que recebe uma frase(frase), coloca todas as letras em minúsculo, tira todos os pontos e inverte a frase
  str -> str'''
  frase = substitui(frase).lower().split()
  frase= frase[::-1]
  frase =' '.join(frase)
  return frase