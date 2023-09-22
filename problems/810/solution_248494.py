def inverte(frase):
    
    """

    
    """
    
    frase0=str.lower(frase)
    frase1=str.replace(frase0,'-',' ')
    frase2=str.replace(frase1,';',' ')
    frase3=str.replace(frase2,':',' ')
    frase4=str.replace(frase3,'.',' ')
    frase5=str.replace(frase4,',',' ')
    frase6=str.replace(frase5,'?',' ')
    frase7=str.replace(frase6,'!',' ')
    
    lista1=str.split(frase7)
    lista2=lista1[::-1]
    
    frase8=str(lista2)
    return ''.join(frase8)