def inverte(frase):
    frase = str.lower(frase)
    frase = str.replace(frase, ",", "")
    frase = str.replace(frase, ".", "")
    lista = str.split(frase, )
    lista = lista.reverse()
    
    return lista[0:]