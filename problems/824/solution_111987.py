def uppCons(frase):
    """Retorna a frase de entrada com todas as consoantes
    maiúsculas;
    str, str -> str"""
    i=0
    upfrase= ''
    while i < len(frase):
        if "aeiouAEIOU" in frase[i]:
            upfrase += frase[i]
        else:
            upfrase += str.upper(frase[i])
    return upfrase