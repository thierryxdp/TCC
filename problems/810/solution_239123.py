def inverte(frase):
    """ Função que recebe uma frase as inverte e retorna uma outra frase
        str->str"""
    frase = str.split(str.join(frase,"!"))-1
    frase = str.split(str.join(frase,"?"))-1
    frase = str.split(str.join(frase,"."))-1
    frase = str.split(str.join(frase,","))-1
    frase = str.split(str.join(frase,"-"))-1
    frase = str.split(str.join(frase,":"))-1
    frase = str.split(str.join(frase,";"))-1
    return frase