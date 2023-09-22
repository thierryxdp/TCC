def freq_palavras(frase):
  """Dada uma frase, a função devolve um dicionário com o numero de vezes que cada
palavra apareceu;
Str -> Dict"""
  lista = str.split (frase, ' ')
  d = {}
  for palavras in lista:
      vezes = str.count(str, palavras)
      d[palavras] = vezes
  return d