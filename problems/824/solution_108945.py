def uppCons(frase):
    """..."""
    contador = 0
    nova_frase = ''
    
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyz':
            str.replace(frase,frase[contador],str.upper(frase[contador]))
            
        contador=contador+1
        
    return frase