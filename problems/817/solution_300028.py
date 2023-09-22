def acima_da_media(nota):
    '''Essa função recebe uma lista de nota e devolve as notas que ficaram
    acima da media'''
    media= sum(nota)/len(nota)
    if media in nota:
    	list.sort(nota)
        lista= lista[list.index(nota,media)+1:]
        #return lista
    else:
        nota.insert(-1,n)
        list.sort(lista_nume)
        lista= nota[list.index(nota,media)+1:]
        #return lista
        return (nota,media)