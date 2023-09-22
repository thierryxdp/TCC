def inverte(frase):
    str1 = ''
    for x in frase:
      	if x != '.' or x != ',' or x != '?' or x != '!':
            str1 += x
    str2 = str1.lower()
    lista = [str2]
    resultado = lista.reverse()
    return resultado