def inverte(string):
    "Funcao que inverte a ordem das palavras na frase dada"
    l = str.split(string)
    l.reverse()
    l = str.join(string,"")
    return string