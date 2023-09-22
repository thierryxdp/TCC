def lingua_p(palavra):
  listpalavra = list(palavra)
  x = 0
  for i in listpalavra:
    x += 1
    if i.lower() in "aeiouáéíóú":
      listpalavra.insert(x, "p"+i)
    
  palavra_p = "".join(listpalavra)
  return palavra_p