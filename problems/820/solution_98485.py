def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    num = []
    while i < len(frase):
        if frase[i] == letra:
            num += [letra]
            num = sum(num)
            if num == ocorrencia:
                ocorre = frase.index(frase[i], i)
                return ocorre
        i += 1
    else:
        return -1