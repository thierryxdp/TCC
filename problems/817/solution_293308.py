def acima_da_media(listaDeNotas):
     media= sum(listaDeNotas)/len(listaDeNotas)
     listaDeNotas.sort()
     return listaDeNotas[listaDeNotas.index(media)+1:]