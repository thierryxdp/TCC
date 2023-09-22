def uppCons(frase):
    """retorna as consoantes em maiusculo enquanto as vogais ficam em minusculo.
    str -> str"""
    contador = 0
    novaFrase = ''
    while contador < len(frase):
        if frase[contador] not in 'aeiouãéíóú':
            novaFrase += frase[contador].upper()
        else:
            novaFrase += frase[contador].lower()
        contador += 1

    return novaFrase