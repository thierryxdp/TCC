def uppCons(frase):
    nova_frase = ""
    for letter in frase:
        if letter in ['a', 'e', 'i', 'o', 'u'] or letter in ['A', 'E', 'I', 'O', 'U']:
            nova_frase += letter.lower()
        else:
            nova_frase += letter.upper()
    return nova_frase[0].upper() + nova_frase[1:]