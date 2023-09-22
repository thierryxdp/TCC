def inverte(frase):
    """ Função """
    frase = str.join(str.split frase,"!")
    frase = str.join(str.split frase,"?")
    frase = str.join(str.split frase,".")
    frase = str.join(str.split frase,",")
    frase = str.join(str.split frase,"-")
    frase = str.join(str.split frase,":")
    frase = str.join(str.split frase,";")
    return frase