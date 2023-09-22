def freq_palavras(frases):
  """Dada uma frase, a função devolve um dicionário com o numero de vezes que cada
palavra apareceu;
Str -> Dict"""
  str.partition (frase, ' ')
  d = {}
  for palavras in frase and palavras != ' ':
    vezes = str.count(frases, palavras)
    d[palavras] = vezes
  return d