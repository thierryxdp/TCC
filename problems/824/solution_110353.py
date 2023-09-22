def uppCons(frase):
    """ Essa função recebe uma frase e retorna todas as con
    soantes em letra maiúsculas. str->str."""
    frase1 = '' 
    primeiro = 0
    vogal = ' '
    while primeiro < len(frase):
        if frase[primeiro] not in 'aeiou':
            frase1 = vogal[primeiro] + str.upper(frase[primeiro],)
        primeiro = primeiro +1 
    return frase1