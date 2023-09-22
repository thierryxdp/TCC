def posLetra(string,letra,n):  
    """
    Função que recebe uma frase, uma letra e um número. Com isso, retornamos a posição da 
    frase que aquela ocorrência da letra está.
    str, str, int -> int
    """
    
    posicao = string.find(letra)
    
    while posicao >= 0 and n > 1:
        posicao = string.find(letra, posicao + 1)
        n = n - 1
    return posicao