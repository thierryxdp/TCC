def freq_palavras(frases):
  '''Função que recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor seu número de repetições
  str -> dict'''

  dicionario = {}
  repeticoes = 0

  for palavra in frases.split(" "):
    '''Para cada palavra na frase'''
    repeticoes = list.count(frases.split(" "),palavra)
    '''É contabilizado seu número de repetições na frase'''
    dicionario[palavra] = repeticoes
    '''A quantidade de repetições correspondente à palavra é indexada no dicionário'''
  return dicionario