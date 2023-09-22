def lingua_p(palavra):
    """Recebe uma palavra e retorna esta 
    traduzida para a 'língua do p'(a letra 
    p seguida envolta na vogal original)
    str -> str"""
    doP = ''
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            doP = doP + letra+'p'+letra
        else:
            doP = doP + letra
    return doP