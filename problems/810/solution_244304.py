def inverte(texto):
    texto = str.replace(texto, ",", "")
    texto = texto[0:-1]
    lista = srt.split(texto, ",")
    lista = list.reverse(lista)
    texto_novo = list.join("", lista)
    
    return lista