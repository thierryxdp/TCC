def posLetra(frase: str, letra:str, ocorrencia:int)-> int:
    """comentário"""
    i = 0
    lista = ()
    while i < len(frase):
        if frase[i] == letra:
            i+=1
        if i == ocorrencia:
                return frase.index(frase[i], i)
        
    else:
        return -1