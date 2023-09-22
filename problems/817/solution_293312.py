def acima_da_media(listaDeNotas):
     media= sum(listaDeNotas)/len(listaDeNotas)
     listaDeNotas.append(media)
     ListaDeNotas.sort()
     return listaDeNotas[listaDeNotas.index(media)+1:]