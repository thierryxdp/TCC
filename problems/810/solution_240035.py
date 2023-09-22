def inverte(txt):
    """Dada uma frase retorna uma outra frase contendo as mesmas palavras da frase de entrada na ordem inversa, sem maiúsculas e sem a pontuação. str->str """
    a = ['!','?','.',',',':',';','-']
    txt = txt.replace(a[0],' ')
    txt = txt.replace(a[1],' ')
    txt = txt.replace(a[2],' ')
    txt = txt.replace(a[3],' ')
    txt = txt.replace(a[4],' ')
    txt = txt.replace(a[5],' ')
    txt = txt.replace(a[6],' ')
    txt = txt.lower()
    txt = str.split(txt)
    txt.reverse()
    return str.join(" ",txt)