def acima_da_media(listaDeNotas):
     Media= sum(listaDeNotas)/len(listaDeNotas)
     ListaDeNotas.sort()
     return listaDeNotas[listaDeNotas.index(media)+1:]