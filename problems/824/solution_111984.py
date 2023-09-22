def uppCons(frase):
    """Retorna a frase de entrada com todas as consoantes
    maiúsculas;
    str, str -> str"""
    i=0
    upfrase= ''
    while i < len(frase):
        if "aeiouAEIOU" not in frase[i]:
            upfrase += str.upper(frase[i])
        elif:
            upfrase += frase[i]
    return upfrase