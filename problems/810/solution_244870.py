def inverte(texto):
    """ Recebe a frase onde todos os caracteres de pontuação ' ,.;:?!' são removidos. String--> String"""
    texto= str.lower(texto)
    texto= texto[0:-1]
    texto= str.replace(texto,",", "")
    texto= str.replace(texto,"-", "")
    texto= str.split(texto,)
    list.reverse()
    a= str.join(" ", list)
    return a