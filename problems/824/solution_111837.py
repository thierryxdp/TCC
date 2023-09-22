def uppCons(frase):
    """comentário"""
    i = 0
    while i < len(frase):
        if frase[i] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvWwXxZzç':
            frase[i].upper()
            frase.replace(frase[i], frase[i])
        i += 1
    return frase