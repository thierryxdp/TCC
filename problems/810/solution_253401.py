def inverte(texto):
    for x in '.:;-,?!':
        texto=texto.replace(x,' ')
    texto1=str.split(texto)
    list.reverse(texto1)
    texto_invertido=str.join(',', texto1)
    return str.lower(texto_invertido.replace(x, '')