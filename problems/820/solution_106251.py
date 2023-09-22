def posLetra(frase,letra,ocorrencia):
    """Determinar a frequência da ocorrencia da letra na frase;
    string, string -> int"""
    vez = 0
    x = 0
    resultado = -1
    while x < len(frase):
        if frase[x].lower() == letra:
            vez +=1
        if vez == ocorrencia:
            resultado = x
            break
        x += 1
    return resultado