def inverte(frase):
    lista = frase.replace('!',' ').replace('?',' ').replace('...',' ').replace('.',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ')
    listasep = lista.split()
    listainterm = listasep.lower()
    listasep2 = listainterm[::-1]
    listafim = " ".join(listasep2)
    return listafim