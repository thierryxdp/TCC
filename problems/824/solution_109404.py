def uppCons(frase):
    """
       """
    nova_frase = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxzç':
            letra = str.upper(letra)
        nova_frase = nova_frase + letra
    return nova_frase