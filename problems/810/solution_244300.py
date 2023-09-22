def inverte(texto):
    texto = str.replace(texto, ",", "")
    lista = texto[0:-1]
    lista = list.reverse(lista)
    
    return lista