def acima_da_media(Notas,Media):
    if Media in Nota:
        ordem = list.sort(Notas)
        return Notas[Media:]
    else:
        list.append(Notas, Media)
        list.sort(Notas)
        ListaMedia = Notas[Media:]
        ListaFinal = list.remove(ListaMedia, Media)
        return ListaFinal