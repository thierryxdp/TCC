def uppCons(frase):
    """Função que recebe uma frase e retorna uma nova frase com todas
    as suas consoantes em letras maiúsculas.
    
    Parameters:
    frase: frase que terá suas consoantes modificadas
    
    Returns:
    Retorna uma nova frase com todas as consoantes maiúsculas
    srt -> str
    """
    i = 0
    frase1 = ''
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            str.upper('frase[i]')
            frase1 = frase1+ frase[i]
        else:
            frase1 = frase1 + frase[i]
        i += 1
    return frase1