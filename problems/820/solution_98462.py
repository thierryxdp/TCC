def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    lista = ()
    while i < len(frase):
        if frase[i] == letra:
            lista += (1,)
            lista = len(lista)
        if lista == ocorrencia:
                return frase.index(frase[i], i)
        i+=1
    else:
        return -1