def acima_da_media(listaDeNotas):
     Media= sum(listaDeNotas)/len(listaDeNotas)
     listaDeNotas.sort()
     return listaDeNotas[listaDeNotas.index(media)+1:]