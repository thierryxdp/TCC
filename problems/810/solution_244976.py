def remove_pontuacao(frase):
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '), '?',' '),'!',' '),'-',' '),',',' '),';',' '),':',' ')

def inverte(frase):
    lista=(str.split(str.lower(remove_pontuacao(frase))))
    list.reverse(lista)
    return str.join(' ', lista)