def uppCons(frase): 
    """funcao que retorna a frase completa, mas com os consoantes em maiusculo;
    str -> str"""
    i=0
    while i<len(frase):
        if frase[i] not in "AEIOUaeiou":
            novafrase=frase[0:i]+str.upper(frase[i])+frase[i+1:]
            i=i+1
        else:
            i=i+1
    return novafrase