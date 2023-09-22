def uppCons(frase):
    """..."""
    contador = 0
    letra = frase[contador]
    frase_nova = ''
  
    
    while contador < len(frase):
        if letra in 'bcdfghjklmnpqrstvwxyz':
            str.upper(letra)
        frase_nova = frase_nova+ letra    
        contador = contador+1
    return frase_nova