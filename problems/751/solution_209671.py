def quant_palavras(frase):
    """A função recebe uma frase em forma de string e retorna o número de 
    palavras dessa frase (int)."""
    if frase[0] == ' ' and frase[-1] == ' ':
        return frase.count(' ') - 1
    if frase[0] == ' ' and frase[-1] != ' ':
        return frase.count(' ')
    if frase[0] != ' ' and frase[-1] == ' ':
        return frase.count(' ')
    else:
        return frase.count(' ') + 1