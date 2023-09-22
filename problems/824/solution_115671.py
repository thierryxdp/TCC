def uppCons(frase):
    """Função que torna maiúcula todas as consoantes de uma frase"""
    """Parâmetros de entrada:str"""
    """Parâmetros de saída:str"""
    i=0
    while i<len(frase):
        if frase[i] not in "AEIOUaeiou":
            frase.upper(frase[1])
        i+=1
    return frase