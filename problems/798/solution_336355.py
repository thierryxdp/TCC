def freq_palavras(frase):
  """Dada uma frase, a função devolve um dicionário com o numero de vezes que cada
palavra apareceu;
Str -> Dict"""
  lista = str.split (frase, ' ')
  d = {}
  for palavras in lista:
      if palavras in 'aeiouAEIOU' and ' ' == lista[list.index(lista, palavras)+1]:
          vezes = str.count(frase, palavras + ' ')
      if palavras in 'aeiouAEIOU' and ' ' == lista[list.index(lista, palavras)-1]:
          vezes = str.count(frase, ' ' + palavras) 
      if palavras not in 'aeiouAEIOU':
          vezes = str.count(frase, palavras)
      d[palavras] = vezes
  return d