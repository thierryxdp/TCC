def inverte(string):
    "Funcao que inverte a ordem das palavras na frase dada"
    l = str.split(string, ' ')
    l.reverse()
    string = str.join(' ',l)
    return string