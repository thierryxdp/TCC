def inverte(frase):
    '''Faça uma função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase
de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.''' 
   #str > str
    frase = str.lower(frase)   
    R = ""
    pont = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in frase:
        if i not in pont:
            R+=i
    lista = str.split(R, " ")
    lista1 = lista[::-1]
    lista2 = str.join(' ', lista1)
    return lista2