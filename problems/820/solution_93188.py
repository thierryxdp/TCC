def posLetra (string, letra, numero):
    """Função que retonar a posição de uma letra dentro de uma string.
    Entrada: string, string, int.
    Saída: int."""
    
    i=0
    repeticoes=0
    
    while i < len(string) and repeticoes<numero:
        if string[i] == letra:
            repeticoes = repeticoes+1
        i=i+1
    if repeticoes<numero:
        return -1
    else:
        return i-1