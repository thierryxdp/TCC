def inverte(frase):
    lista = frase.replace('!',' ').replace('?',' ').replace('...',' ').replace('.',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ')
    listasep = lista.split()
    listasep2 = listasep[-1:]
    listafim = listasep2.join()
    return listafim