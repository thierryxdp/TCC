def uppCons(frase):
    """retorna a frase de entrada com as consoantes
    em maiusculas"""
    count=0
    while count<len(frase):
        if frase[count] not in "AEIOUaeiou":
            frase=frase.upper([count])
        count=count+1
    return frase