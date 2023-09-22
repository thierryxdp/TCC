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
    frase1= str.split(frase)
    while i < len(frase):
        if str.lower(frase[i]) not in "aeiou":
            index = str.index(frase1, frase[i])
            del frase1[index]
            list.insert(frase1,index, str.upper(frase[i]))
        i += 1
    return str.join(' ', lista1)