def uppCons(frase):
    """
    Dada uma frase, a função retorna todas as consoantes em maiusculo enquanto as vogais permanecem em
    minusculo.
    str-> str
    """
    contador = 0
    novafrase = ''
    while contador < len(frase):
        if frase[contador] not in 'aeiouãéíóú':
            novafrase += frase[contador].upper()
        else:
            novafrase += frase[contador].lower()
        contador += 1

    return novafrase