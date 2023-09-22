def inverte(frase):
    """função que retira as pontuações, letras maiusculas e inverte as frases
    str -> str"""
    frase1 = str.replace(frase,',',' ')
    frase2 = str.replace(frase1,'-',' ')
    frase3 = str.replace(frase2,':',' ')
    frase4 = str.replace(frase3,';',' ')
    frase5 = str.replace(frase4,'.',' ')
    frase6 = str.replace(frase5,'!',' ') 
    frase7 = str.replace(frase6,'...',' ')
    frase8 = str.replace(frase7,'?',' ')
    frase9 = str.lower(frase8)
    return frase9