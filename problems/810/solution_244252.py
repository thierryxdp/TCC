def inverte(frase):
    frase = str.lower(frase)
    frase = str.replace(frase, ",", "")
    frase = str.replace(frase, ".", "")
    lista = str.split(frase, )
    liste = list.reverse(lista)
    
    return lista