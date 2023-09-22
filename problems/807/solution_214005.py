def conta_frases(texto):
        novotexto=str.replace(texto,"...",".",-1)
        return str.count(novotexto,"!") + str.count(novotexto,"?") + str.count(novotexto,".")