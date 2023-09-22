def inverte(frase):
    frase1=str.replace(frase, '.',' ')
    frase2=str.replace(frase, '!',' ')
    frase3=str.replace(frase, '?',' ')
    frase4=str.replace(frase, '...',' ')
    frase5=str.replace(frase, ',',' ')
    frase6=str.replace(frase, '-',' ')
    frase7=str.replace(frase, ':',' ')
    frase8=str.replace(frase, '.;',' ')
    frase9=str.lower(frase8)
    frase10=str.split(frase9)
    frase11=frase10[::-1]
    frase12=str(frase11)
    frase13=str.replace(frase12, '[','')
    frase14=str.replace(frase13, ']','')
    frase15=str.replace(frase14, ',','')
    frase16=str.replace(frase15, "'",'')
    return frase16