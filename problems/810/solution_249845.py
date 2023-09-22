def inverte(frase):
    '''
    '''
    um = str.replace(frase,'-',' ')
    dois = str.replace(um,',',' ') 
    tres = str.replace(dois,':',' ')
    quatro = str.replace(tres,';',' ')
    cinco = str.replace(quatro,'.',' ')
    seis = str.replace(cinco,'?',' ')
    sete = str.replace(seis,'!',' ')
    
    k = str.lower(sete)
    
    w = str.split(k)
    
    o = list(reversed(w))
    
    b = ' '.join(o)
    
    return b