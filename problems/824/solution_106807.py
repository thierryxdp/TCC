def uppCons(frase):
    """Retorna a frase com consoantes maiusculas e demais caracteres originais. str--str"""
    i=0
    while i<(len(frase)-1):
        if frase[i] not in "AEIOUaeiou":
            frase[i]=str.upper(frase[i])
        else:
            frase[i]=frase[i]
        i=i+1
        return frase