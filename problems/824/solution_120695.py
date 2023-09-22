def uppCons(frase):
  vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  nova = []
  c = 0
  while c != len(frase):
    if frase[c] in 'aeiouAEIOU':
      nova.append(frase[c])
    elif frase[c] not in 'aeiouAEIOU':
      if frase[c].isupper == True:
        nova.append(frase[c])
      else:
        f1 = frase[c].swapcase()
        nova.append(f1)
    c += 1
  return ''.join(nova)