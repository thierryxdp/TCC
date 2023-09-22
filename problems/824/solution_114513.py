def uppCons(frase):
    """
    Dada uma frase, a função retorna todas as consoantes em maiusculo enquanto as vogais permanecem em
    minusculo.
    str-> str
    """
    i = 0
    novafrase = []
    while i < len(frase):
        if frase[i] not in 'aeiouãéíóú':
            novafrase += frase[i].upper()
        else():
             novafrase += frase[i].lower()
                i += 1
                
                return novafrase