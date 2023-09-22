def inverte(frase):
    str1 = ''
    for x in frase:
      	if x != '.' or x != ',' or x != '?' or x != '!':
            str1 += x
   	str1 = str1.lower()
    lista = [str1]
    resultado = lista.reverse()
    return resultado