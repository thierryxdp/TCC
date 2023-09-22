def lingua_p(palavra):
  palavra = palavra.lower()
  vogais = ['a', 'e', 'i', 'o', 'u']
  #palavraFinal = palavra
  #contAdicionados = 0
  for i in range(len(palavra)):
    charAtual = palavra[i]
    if charAtual in vogais:
      subs = charAtual + 'p' + charAtual
      #palavraFinal = palavraFinal[:i + contAdicionados] + subs + palavraFinal[i + contAdicionados:]
      palavra = palavra[:i] + subs + palavra[i:]
      i += 2
      #contAdicionados += 2
  return palavraFinal