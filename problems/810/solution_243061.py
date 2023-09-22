def inverte(frase):
    """remove a pontuacao e inverte"""
    frase1 = str.replace(frase,'.',' ',100)
    frase2 = str.replace(frase1,',',' ', 100)
    frase3 = str.replace(frase2,'-',' ', 100)
    frase4 = str.replace(frase3,'?',' ', 100)
    frase5 = str.replace(frase4,':',' ', 100)
    frase6 = str.replace(frase5,';',' ', 100)
    frase7 = str.replace(frase6,'!',' ', 100)
    lower = str.lower(frase7)
    fraselista = lower.split( )
    reverse = list.reverse(fraselista)
    return str.join(' ',fraselista)