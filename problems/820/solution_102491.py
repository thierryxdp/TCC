def posLetra(texto:str,letra:str,num:int)-> str:
    """Recebe um texto, uma letra e sua ocorrência e retorna seu exato índice."""
    ocorrencia=0
    i=0
    if num>str.count(texto,letra):
        ocorrencia=-1
    while i<len(texto):
        if letra in texto[i]:
            ocorrencia += 1
        elif letra in texto[i] and ocorrencia==num:
            ocorrencialetra= str.index(texto,letra,i)
        i=i+1  
    return ocorrencialetra