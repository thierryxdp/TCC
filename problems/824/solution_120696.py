def uppCons(frase):
  nova = []
  c = 0
  while c != len(frase):
    if frase[c] in 'aeiouAEIOU':
      nova.append(frase[c])
    else:
      x = frase[c].isupper()
      if x == True:
        nova.append(frase[c])
      else:
        f1 = frase[c].upper()
        nova.append(f1)
    c += 1
  return ''.join(nova)