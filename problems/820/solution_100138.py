def posLetra(string,letra,n):  
    """
    Função que recebe uma frase, uma letra e um número. Com isso, retornamos a posição da 
    frase que aquela ocorrência da letra está.
    str, str, int -> int
    """
    
    pos = string.find(letra)
    while pos >= 0 and n > 1:
        pos = string.find(letra, pos + 1)
        n -= 1
    return pos