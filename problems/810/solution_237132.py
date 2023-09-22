def inverte(frase):
  frase = retira_pontuacao(frase)
  lista = frase.split(' ')
  lista.reverse()
  lista.remove('')
  frase = str.join(' ', lista)
  return frase