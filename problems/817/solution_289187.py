def acima_da_media(lista):
  media = sum(lista) / len(lista)
  acima da media = len([n for n in lista if n > media])
    return acima da media