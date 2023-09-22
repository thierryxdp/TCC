def uppCons(frase):
    """Função que torna maiúcula todas as consoantes de uma frase"""
    """Parâmetros de entrada:str"""
    """Parâmetros de saída:str"""
    contador=0
    acumulador=""
    while contador<len(frase):
        if frase[contador] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
            acumulador+=str.upper(frase[contador])
        contador+=1  
    return acumulador