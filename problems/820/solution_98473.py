def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    lista = ()
    while i < len(frase):
        if frase[i] == letra:
            lista = lista + (1,)
            lista = len(lista)
            if i == ocorrencia:
                ocorre = frase.index(frase[i], i)
                return ocorre
        i += 1
    else:
        return -1