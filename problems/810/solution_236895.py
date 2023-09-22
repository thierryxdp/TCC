def inverte(frase):
    R = ""
    pont = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    pont = ''','''
    for i in frase:
        if i in pont:
            frase = frase.replace(i, " ")
        for i in frase:
            if i in pont:
               frase = frase.replace(i, "") 
    frase = str.strip(frase)
    frase = str.lower(frase)
    lista = str.split(frase, " ")
    lista1 = lista[::-1]
    lista2 = str.join(' ', lista1)
    return lista2