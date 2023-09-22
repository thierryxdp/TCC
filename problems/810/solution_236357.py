def inverte(frase):
    frase = str.lower(frase)
    R = " "
    pont = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in frase:
        if i not in pont:
            R+=i
    lista = str.split(R, " ")
    lista1 = lista[::-1]
    lista2 = str.join(' ', lista1)
    return lista2