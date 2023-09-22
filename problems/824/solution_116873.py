def uppCons(frase):
    """A função recebe como entrada uma string contendo
    uma frase e retorna a mesma string, mas com todas as
    consoantes em maiúsculas."""
    frase_nova = ''
    vogais = 'AEIOUaeiouãõÃÕâêôÂÊÔáéíóúÁÉÍÓÚ'
    i = 0
    
    while i < len(frase):
        if frase[i] not in vogais:
            frase_nova = frase_nova + (frase[i]).upper()
            i += 1
        else:
            frase_nova = frase_nova + frase[i]
            i += 1
    return frase_nova