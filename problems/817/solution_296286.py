def acima_da_media(notas):
   media= sum(notas)/len(notas)
   list.insert(notas,0,media)
   list.sort(notas)
   x=list.index(notas,media)
   if media in lista[x+1]:
    list.remove(media)
   return notas[x+1:]