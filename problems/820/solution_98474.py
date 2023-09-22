def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    num = 0
    while i < len(frase):
        if frase[i] == letra:
            num += 1
            if i == ocorrencia:
                ocorre = frase.index(frase[i], i)
                return ocorre
        i += 1
    else:
        return -1