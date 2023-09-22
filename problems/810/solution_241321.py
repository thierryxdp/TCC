def inverte(frase):
    listalower = frase.lower()
    lista = listalower.replace('!',' ').replace('?',' ').replace('...',' ').replace('.',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ')
    listasep = lista.split()
    listasep2 = listasep[::-1]
    listafim = " ".join(listasep2)
    return listafim