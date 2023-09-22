def inverte(frase):
    """Função que dada uma frase retorna uma outra frase que contenha as
    mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas
    e sem pontuação.
    str->str
    """
	a = str.replace(str.replace(str.replace(str.replace\
        (str.replace(frase,',',' '),'.',' '),'?',' '),'!',' '),';',' ')
    x = a.split()
    z = x[len(x)::-1]
    y = str.join(' ',z)
    w = str.lower(y)
    return w