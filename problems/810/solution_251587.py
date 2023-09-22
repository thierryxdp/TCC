def inverte(frase):
  x=str.replace(frase, "...", "")
  x=str.replace(x, "?", "")
  x=str.replace(x, "!", "")
  x=str.replace(x, ".", "")
  x=str.replace(x, ":", "")
  x=str.replace(x, ":", "")
  x=str.replace(x, "-", " ")
  x=str.replace(x, ",", "")
  x=str.lower(x)
  x=str.split(x, " ")
  i=0
  salva_valor = ""
  while i < len(x)/2:
    salva_valor = x[len(x)-(i+1)]
    x[len(x)-(i+1)] = x[i]
    x[i] = salva_valor
    i += 1
  x = str.join(" ", x)
  return x