def uppCons(frase):
    """Funcao que dada uma frase retorna com todas as consoantes
    maiusculas e os demais caracteres como estavam antes
    str -->str"""
    frase_nova = ""
    i = 0
    while i < len(frase):
        palavra = frase[i]
        if palavra not in "aãâáàeéêiíîoõóôuú":
            x = str.upper(palavra)
            frase_nova = frase_nova + x
        else:
            frase_nova = frase_nova + palavra
        i = i + 1
    return frase_nova