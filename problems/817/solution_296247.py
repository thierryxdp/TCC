def acima_da_media(notas):
   media= sum(notas)/len(notas)
   y=len(notas)
   list.insert(notas,0,media)
   list.sort(notas)
   x=list.index(notas,media)
    if y>1:
        return notas[x+1:]
    if y==1:
        return []