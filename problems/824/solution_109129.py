def uppCons(frase):
    """Dada uma frase retorna esta com suas consoantes em maiúsculo.
       str -> str"""
    
    contador = 0
    novaFrase = ' '
    
    while contador < len(frase):
        if frase[contador] in 'qwrtypsdfghjklzxcvbnm':
            a = frase[contador].upper()
            novaFrase += a
            contador = contador + 1
        return novaFrase