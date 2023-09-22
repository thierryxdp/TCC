def acima_da_media(listaDeNotas):
     media= sum(listaDeNotas)/len(listaDeNotas)
     listaDeNotas.append(int(media))
     listaDeNotas.sort()
     return listaDeNotas[listaDeNotas.index(int(media))+(list.count(listaDeNotas,media)):]