def retira_pontuacao(frase):
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