def lingua_p (palavra):
    """funçao que recebe uma palavra em portugues e retorna a palavra na lingua do p;
entrada: str;
saida: str."""
    palavra = str.lower(palavra)
    p = ''
    for elemento in range (len (palavra)):
        if palavra[elemento] in 'aeiouáàéèãíóú':
            p += palavra[elemento] + 'p' + palavra[elemento]
        else:
            p += palavra[elemento]
    return p