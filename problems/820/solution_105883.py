def posLetra(frase,letra,n):
    """
    Função que recebe uma string (frase), uma letra (letra)
    e um numero de ocorrencia (n) desejada da letra nesta frase.
    retorna a posição da string em que a letra está
    str, str, int -> int
    """
    
    procurar = frase.find(letra)
    
    while procurar >= 0 and n > 1:
        procurar = frase.find(letra, procurar+1)
        n -= 1
    return procurar