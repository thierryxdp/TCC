def uppCons(frase):
    """Dada uma frase retorna esta com suas consoantes em maiúsculo.
       str -> str"""
    
    contador = 0
    novaFrase = ' '
    
    while contador < len(frase):
        if frase[contador] in 'qwrtypsdfghjklzxcvbnm':
            novaFrase = frase[contador].upper() + novaFrase
            contador = contador + 1
        else:
            novaFrase = frase[contador] + novaFrase
            contador = contador + 1
        
        return novaFrase