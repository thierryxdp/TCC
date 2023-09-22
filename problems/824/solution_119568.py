def uppCons (frase):
    """retorna uma frase de entrada com todas suas consoantes em maiúsculas"""
    nova_frase = ''
    for letra in frase:
        if letra not in 'aeiou':
            nova_frase += letra.upper()
        if letra in 'aeiou':
            nova_frase += letra
    return nova_frase