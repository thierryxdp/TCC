def inverte(frase):
    lista = frase.replace('!',' ').replace('?',' ').replace('...',' ').replace('.',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ')
    listasep = lista.split()
    listasep2 = listasep[-0:]
    listafim = "".join(listasep2)
    return listafim