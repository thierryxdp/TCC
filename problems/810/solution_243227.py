def inverte(frase):
    pont1 = ','
    pont2 = '.'
    pont3 = '-'
    pont4 = '?'
    pont5 = '!'
    frase1 = str.replace(frase,pont1,' ')
    frase2 = str.replace(frase1,pont2,' ')
    frase3 = str.replace(frase2,pont3,' ')
    frase4 = str.replace(frase3,pont4,' ')
    frase5 = str.replace(frase4,pont5,' ')
    return frase5