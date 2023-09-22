def uppCons(frase):
    """
    Dada uma frase, retorna outra frase cujas consoantes estao em
    maiusculo. Os outros caracteres permanecem iguais
    Entrada:
    	frase: string
    Returns:
    	string
    """
    i = 0
    nova_frase = ''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            nova_frase = nova_frase + str.upper(frase[i])
        else:
            nova_frase = nova_frase + frase[i]
        i = i + 1
    return nova_frase