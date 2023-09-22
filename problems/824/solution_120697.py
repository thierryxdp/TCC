def uppCons(frase):
  nova = []
  c = 0
  while c != len(frase):
    if frase[c] not in 'aeiouAEIOU':
      x = frase[c].isupper()
      if x == True:
        nova.append(frase[c])
      else:
        f1 = frase[c].upper()
        nova.append(f1)
    else:
      nova.append(frase[c])
    c += 1
  return ''.join(nova)