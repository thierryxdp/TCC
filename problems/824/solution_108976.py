def uppCons(frase):
    """..."""
    contador = 0
    frase_nova = ''
  
    
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyzç:
            x = str.upper(frase[contador])
        else:
            x = frase[contador]
        frase_nova = frase_nova + x 
        contador = contador+1
    return frase_nova