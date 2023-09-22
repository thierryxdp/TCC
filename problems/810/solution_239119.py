def inverte(frase):
    """ Função que recebe uma frase as inverte e retorna uma outra frase
        str->str"""
    frase = str.join(str.split frase,"!")-1
    frase = str.join(str.split frase,"?")-1
    frase = str.join(str.split frase,".")-1
    frase = str.join(str.split frase,",")-1
    frase = str.join(str.split frase,"-")-1
    frase = str.join(str.split frase,":")-1
    frase = str.join(str.split frase,";")-1
    return frase