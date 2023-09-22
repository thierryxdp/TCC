def uppCons(frase):
    """Funcao que recebe uma frase e retorne a mesma com todas
    as suas consoantes em maiusculas e os demias caracteres nao devem 
    mudar."""
    i = 0
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOUãáàéèíóôú':
            frase= frase.replace(frase[i],frase[i].upper())
            i = i + 1
            return frase