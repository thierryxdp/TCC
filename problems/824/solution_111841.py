def uppCons(frase):
    """comentário"""
    i = 0
    while i < len(frase):
        if frase[i] in 'BbCcçÇDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvWwXxZz':
            frase = frase.replace(frase[i], frase[i].upper())
        i += 1
    return frase