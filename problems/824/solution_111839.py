def uppCons(frase):
    """comentário"""
    i = 0
    while i < len(frase):
        if frase[i] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvWwXxZzç':
            frase = frase.replace(frase[i], frase[i].upper())
        i += 1
    return frase