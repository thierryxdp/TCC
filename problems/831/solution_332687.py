def lingua_p(palavra):
  palavra = palavra.lower()
  vogais = ['a', 'e', 'i', 'o', 'u']
  #palavraFinal = palavra
  #contAdicionados = 0
  i = 0
  while i < len(palavra):
    print(palavra)
    print(i)
    charAtual = palavra[i]
    if charAtual in vogais:
        subs = charAtual + 'p' + charAtual
        palavra = palavra[:i] + subs + palavra[-(len(palavra) - (i + 1)):]
        i += 2

    i += 1
  return palavra