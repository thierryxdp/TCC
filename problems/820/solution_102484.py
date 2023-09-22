def posLetra(texto:str,letra:str,num:int)-> str:
    """Recebe um texto, uma letra e sua ocorrência e retorna seu exato índice."""
    ocorrencia=0
    i=0
    if num>str.count(texto,letra):
        ocorrencia=-1
    while i<len(texto):
        if ocorrencia==num in texto[i]:
            ocorrencialetra=str.index(texto,letra)
            ocorrencia +=1
        i=i+1  
    return ocorrencia