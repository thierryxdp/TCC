def acima_da_media(notas):
   media = sum(notas)/len(notas)
   notas.sort()
   return [x for x in notas if x > media]