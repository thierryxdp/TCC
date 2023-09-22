def acima_da_media(listaDeNotas):
     media= int(sum(listaDeNotas)/len(listaDeNotas))
     listaDeNotas.append(media)
     listaDeNotas.sort()
     return listaDeNotas[listaDeNotas.index(media)+2:]