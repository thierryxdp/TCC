#Start your python function here
def filtra_pares(tupla):
    
    primeiro= (tupla[0],)
    segundo= (tupla[1],)
    terceiro= (tupla[2],)
    quarto= (tupla[3],)
    
    filt_tupla=('nada ainda',)
    
    if primeiro%2==0:
        
        filt_tupla=filt_tupla,primeiro
        
    elif segundo%2==0:
        
        filt_tupla=filt_tupla,segundo
        
    elif terceiro%2==0:
        
        filt_tupla=filt_tupla,terceiro
        
    elif quarto%2==0:
        
        filt_tupla=filt_tupla,quarto
    return filt_tupla[1:]