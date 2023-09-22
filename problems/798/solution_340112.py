def freq_palavras(frase):
  listfrase = frase.split(" ")
  frasedict = {}
  a = 0
  while a < len(listfrase):
    b = a + 1
    count = 1
    while b < len(listfrase):
      if listfrase[a] == listfrase[b]:
        count+=1
        listfrase[b] = ""
      b+=1
    frasedict.update({listfrase[a]:count})
    a+=1
  frasedict.pop("")
  return frasedict