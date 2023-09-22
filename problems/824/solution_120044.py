def uppCons(string):
  txt = list(string)
  print(txt)
  i = 0
  while i < len(txt):
    print(txt[i].lower())
    if txt[i].lower() != "a" and txt[i].lower() != "e" and txt[i].lower() != "i" and txt[i].lower() != "o" and txt[i].lower() != "u":
         txt[i] = txt[i].upper()
    i+=1
  txt = "".join(txt)
  return txt