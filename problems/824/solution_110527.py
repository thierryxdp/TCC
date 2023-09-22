def uppCons(frase):
    """ Essa função recebe uma frase e retorna todas as con
    soantes em letra maiúsculas. str->str."""
    frase1 = '' 
    primeiro = 0
    while primeiro < len(frase):
        if frase[primeiro] not in 'aeiou':
            str.upper(frase[primeiro])
        primeiro = primeiro +1 
    return frase