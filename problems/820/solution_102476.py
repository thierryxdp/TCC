def posLetra(texto:str,letra:str,num:int)-> str:
    """Recebe uma frase e retorna ela com todas as suas consoantes maiúsculas"""
    ocorrencia=-1
    i=0
    if num>str.count(texto,letra):
           return ocorrencia
    while i<len(texto):
        if letra in texto:
            ocorrencia = str.index(texto,letra,num-1)
        i=i+1  
    return ocorrencia