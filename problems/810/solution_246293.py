def inverte(frase):
  frase1 = frase.replace("...", " ")
  frase2 = frase1.replace("!"," ")
  frase3 = frase2.replace("?"," ")
  frase4 = frase3.replace(";"," ")
  frase5 = frase4.replace("."," ")
  frase6 = frase5.replace("-"," ")
  frase7 = frase6.replace(":", " ")
  frase8 = frase7.replace(","," ")
  frase9 = frase8.split(" ")
  frase9.reverse()
  s= ' '
  frase10 = s.join(frase9)
  frase11 = str.lower(frase10)
  frase12 = frase11.replace("  "," ")
  return frase11