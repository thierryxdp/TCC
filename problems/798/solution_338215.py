#1
'''
retorna dicionario da string
string -> dict
'''
def freq_palavras(words):
  counter = dict()
  words = words.split()

  for word in words:
      if word in counter:
          counter[word] += 1
      else:
          counter[word] = 1

  return counter