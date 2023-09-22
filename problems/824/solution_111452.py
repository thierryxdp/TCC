def uppCons(frase):
    """função que recebe uma frase e retorna a mesma com 
    todas as suas consoantes maiusculas.
    str -> str"""
    i = 0
    nova_frase = ''

    while i < len(frase):
        letra = frase[i]
        if letra in 'aeiou':
            nova_frase += str(letra)
        else:
            nova_frase += str(letra.upper())
        i = i + 1

    return nova_frase