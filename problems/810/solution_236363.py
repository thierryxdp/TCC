def inverte(frase):
    '''Faça uma função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase
de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.''' 
   #str > str
    R = ""
    pont = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in frase:
        if i in pont:
            frase = frase.replace(i, " ")
    frase = str.strip(frase)
    frase = str.lower(frase)
    lista = str.split(frase, " ")
    lista1 = lista[::-1]
    lista2 = str.join(' ', lista1)
    return lista2