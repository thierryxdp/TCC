def uppCons (frase) :
    """Funcao que recebe uma frase e retorna esta frase com todas suas consoantes em maiúsculas"""
    contador = 0
    while contador < len(frase):
        if frase[contador] not in 'aeiouAEIOUãáàéèíóôú':
            frase = frase.replace(frase[contador],frase[contador].upper())
        contador = contador + 1
    return frase