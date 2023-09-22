def posLetra(frase,letra,ocorrencia):
    """retorna em que posição da string aquela ocorrência da letra esta; str, str, int -> int"""
    a=0
    b=[]
    if ocorrencia > str.count(frase,letra):
        return -1
    while a < len(frase):
        if frase[a]==letra:
            b=b+[letra]
        a=a+1
    return b[ocorrencia]