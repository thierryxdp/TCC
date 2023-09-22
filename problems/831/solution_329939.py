def lingua_p(palavra):
    """
    Retorna a palavra na lingua P.
    str -> str
    """
    vogais=[a,e,i,o,u]
    for i in range(0,len(palavra)):
        if palavra[i] in vogais:
            palavra_p = palavra[0:i+1]+'p'+palavra[i:]
        return palavra_p