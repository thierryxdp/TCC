def posLetra (string, letra, numero):
    """Função que retonar a posição de uma letra dentro de uma string.
    Entrada: string, string, int.
    Saída: int."""
    
    i=0
    repetições=0
    
    while i < len(string) and repetições<numero:
        if string[i] == letra:
            repetições = repetições+1
        i=i+1
    if repetições<numero:
        return -1
    else:
        return x-1