def posLetra (frase, letra, n):
    """fucao que indica o indice da ocorrencia de numero n da letra informada na
    frase fornecida
    
    str, str, int -> int
    """
    
    i=0
    
    while i<=n:
        posicao = list.index(frase, letra,i:)
        i=i+1
        return posicao