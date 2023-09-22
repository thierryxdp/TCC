def acima_da_media(lista):
  media = sum(lista) / len(lista)
  return len([n for n in lista if n > media])