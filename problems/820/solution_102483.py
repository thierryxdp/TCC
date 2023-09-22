def posLetra(texto:str,letra:str,num:int)-> str:
    """Recebe um texto, uma letra e sua ocorrência e retorna seu exato índice."""
    ocorrencia=0
    i=0
    if num>str.count(texto,letra):
        ocorrencia=-1
        return ocorrencia
    while i<len(texto):
        if letra in texto:
            ocorrencia = str.index(texto,letra,num)
        i=i+1  
    return ocorrencia