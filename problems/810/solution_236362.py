def inverte(frase):
    '''Faça uma função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase
de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.''' 
   #str > str
    frase = str.lower(frase)
    lista = str.split(frase, " ")
    lista1 = lista[::-1]
    lista2 = str.join(' ', lista1)
    R = ""
    pont = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in lista2:
        if i in pont:
            lista2 = lista2.replace(i, " ")
    return lista2