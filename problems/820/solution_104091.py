def posLetra(frase,letra,numero):
    """A função recebe uma frase, uma letra e um número e retorna em
    que posição da string aquela ocorrência da letra está. Caso não 
    exita ocorrências suficinte, retorna -1.
    assinatura: str, str, int --> int"""
    o = 0
    for i in range (len(frase)):
        if o == numero:
            return i-1
        if frase [i] == letra:
            o += 1
    if o < numero:
            return -1