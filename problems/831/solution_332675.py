def lingua_p(palavra):
  palavra = palavra.lower()
  vogais = ['a', 'e', 'i', 'o', 'u']
  
  for i in range(len(palavra)):
    charAtual = palavra[i]
    if charAtual in vogais:
      subs = charAtual + 'p' + charAtual
      palavra = palavra[:i] + subs + palavra[i:]
  return palavra