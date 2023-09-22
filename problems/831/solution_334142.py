def lingua_p(palavra):
  listpalavra = list(palavra)
  x = 0
  for i in listpalavra:
    x += 1
    if i.lower() in "aeiou":
      listpalavra.insert(x, "p")
  palavra_p = "".join(listpalavra)
  return palavra_p