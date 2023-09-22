def inverte(frase):
    """ Função que recebe uma frase as inverte e retorna uma outra frase
        str->str"""
    frase = str.join(str.split frase,"!")
    frase = str.join(str.split frase,"?")
    frase = str.join(str.split frase,".")
    frase = str.join(str.split frase,",")
    frase = str.join(str.split frase,"-")
    frase = str.join(str.split frase,":")
    frase = str.join(str.split frase,";")
    return frase