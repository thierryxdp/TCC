def uppCons(frase):
    """Funcao que dada uma frase retorna com todas as consoantes
    maiusculas e os demais caracteres como estavam antes
    str -->str"""
    frase_nova = ""
    palavra = 0
    while palavra < len(frase):
        if frase[palavra] == "a" or "e" or "i" or "o" or "u":
            frase_nova = frase_nova + frase[palavra]
        else:
            x = str.upper(frase[palavra])
            frase_nova = frase_nova + x
        palavra = palavra + 1
    return frase_nova