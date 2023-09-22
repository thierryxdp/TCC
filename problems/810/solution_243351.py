def inverte(frase):
    """função que retorna a frase sem pontuação e em ordem invertida
    str -> str"""
    frase1 = str.replace(frase,',',' ')
    frase2 = str.replace(frase1,'-',' ')
    frase3 = str.replace(frase2,':',' ')
    frase4 = str.replace(frase3,';',' ')
    frase5 = str.replace(frase4,'.',' ')
    return frase5