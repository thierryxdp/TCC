def uppCons(frase):
    """Retorna a frase com consoantes maiusculas e demais caracteres originais. str--str"""
    i=0
    j=frase[i]
    frase_final=""
    while i<(len(frase)-1):
        if j not in "AEIOUaeiou":
            j=str.upper(frase[i])
            frase_final=frase_final+j
        else:
            j=frase[i]
            frase_final=frase_final+j        
        i=i+1
        return frase_final