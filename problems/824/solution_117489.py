def uppCons(frase):
    """Funcao que dada uma frase retorna com todas as consoantes
    maiusculas e os demais caracteres como estavam antes
    str -->str"""
    frase_nova = ""
    i = 0
    while i < len(frase):
        palavra = frase[i]
        if palavra == "a" or "e" or "i" or "o" or "u":
            frase_nova = frase_nova + palavra
        else:
            x = str.upper(palavra)
            frase_nova = frase_nova + x
        palavra = palavra + 1
    return frase_nova