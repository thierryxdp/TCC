def inverte(frase):
    """função que dada uma frase retorna uma outra frase que contenha as
    mesmas palavras da frase de entrada na ordem inversa, sem letras maiusculas
    e sem pontuação.
    str -> str
    """

    a =  str.replace(str.replace(str.replace(str.replace\
         (str.replace(frase,',',' '),'.',' '),'?',' '),'!',' '),'-',' ')
    b = a.split()
    c = b[len(b)::-1]
    d = str.join(' ',c)
    e = str.lower(d)
    return e