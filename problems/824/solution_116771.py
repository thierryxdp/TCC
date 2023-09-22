def uppCons(frase):
    """A função recebe como entrada uma string contendo uma 
    frase e retorna outra string com a mesma frase, porém
    com as consoantes todas maiúsculas."""
    frase_nova = ' '
    i = 0
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOU':
            cons = str.upper(frase[i])
        frase_nova = frase_nova + frase[i] + cons
        i += 1
    return frase_nova