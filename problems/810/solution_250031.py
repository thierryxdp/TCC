def inverte (frase):
    '''retorna '''
    frase1= str.replace(frase,'!','')
    frase2= str.replace(frase1,'?','')
    frase3= str.replace(frase2,'.','')
    frase4= str.replace(frase3,',','')
    frase5= str.replace(frase4,'-','')
    frase6= str.lower(frase5)
    frase7= list.reverse(frase6)
    return frase7