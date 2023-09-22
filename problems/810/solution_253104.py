def inverte(frase):
  '''Função que recebe uma frase(frase), coloca todas as letras em minúsculo, tira todos os pontos e inverte a frase
  str -> str'''
  frase = substitui(frase).lower().split()
  frase= frase[::-1]
  frase =' '.join(frase)
  return frase