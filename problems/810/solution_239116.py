def inverte(frase):
    """ Função """
    frase = str.split(str.join frase,"!")
    frase = str.split(str.join frase,"?")
    frase = str.split(str.join frase,".")
    frase = str.split(str.join frase,",")
    frase = str.split(str.join frase,"-")
    frase = str.split(str.join frase,":")
    frase = str.split(str.join frase,";")
    return frase