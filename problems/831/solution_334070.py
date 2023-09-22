# Questão 3
def lingua_p(frase):
  frase.lower()
  nf = list(frase)
  for c in range(len(nf)):
    if nf[c] in 'aeiou':
      nf.insert(c+1, 'p')
      nf.insert(c+2, nf[c])
      c +=1
  x = ''.join(nf)
  return x