def acima_da_media(listaDeNotas):
     media= sum(listaDeNotas)/(len(listaDeNotas)+1)
     listaDeNotas.append(media)
     listaDeNotas.sort()
     return listaDeNotas[(listaDeNotas.index(media)+1):]