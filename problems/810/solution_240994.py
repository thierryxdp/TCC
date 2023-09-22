def inverte(frase):
    lista1=list(frase)
    lista2=' '.join(lista1)
    frase8=lista2[-1:0]
    frase1=frase8.replace('.',' ')
    frase2=frase1.replace(',',' ')
    frase3=frase2.replace('-',' ')
    frase4=frase3.replace(':',' ')
    frase5=frase4.replace(';',' ')
    frase6=frase5.replace('!', ' ')
    frase7=frase6.replace('?', ' ')
    
    return frase7