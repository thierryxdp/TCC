def conta_frases(texto):
    """ Essa função retorna a quantidade de frases existentes no texto introduzido. Str->int """
    texto = texto.replace("...",".")
    return (str.count(texto,"!") + str.count(texto,"?") + str.count(texto,"."))