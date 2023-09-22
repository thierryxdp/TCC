def remove_pontuacao(frase):
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '), '?',' '),'!',' '),'-',' '),',',' '),';',' '),':',' ')

def inverte(frase):
    lista=remove_pontuacao(frase)
    lista=str.lower(lista)
    lista=str.split(lista)
    list.reverse(lista)
    lista= str.join(' ', lista)
    return lista