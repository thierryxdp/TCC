def uppCons(frase):
    """Retorna a frase de entrada com todas as consoantes
    maiúsculas;
    str, str -> str"""
    i=0
    upfrase= ''
    while i < len(frase):
        if frase[i] in "aeiouáéíóúÃÀAEIOU" :
            upfrase += frase[i]
        else:
            upfrase += str.upper(frase[i])
        i+=1
    return upfrase