def uppCons(frase):
    """
    Transforma as consoantes de uma frase em letras maiúsculas.
    str -> str

    Parameters:
    frase: Parâmetro textual, do tipo string (str).

    Returns:
    A frase alterada.
    """

    i = 0
    nova_frase = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    frase = list(frase)

    while i < len(frase):
        if frase[i] in vogais:
            nova_frase.extend(frase[i])
        else:
            nova_frase.extend(str.upper(frase[i]))
        i = i + 1
    
    nova_frase = ''.join(nova_frase)

    return nova_frase