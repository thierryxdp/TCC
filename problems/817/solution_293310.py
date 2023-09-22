def acima_da_media(listaDeNotas):
     media= sum(listaDeNotas)/len(lista)
     lista.append(media)
     ListaDeNotas.sort()
     return lista[lista.index(media)+1:]