def uppCons(frase):
    """ Essa função recebe uma frase e retorna todas as con
    soantes em letra maiúsculas. str->str."""
    frase1 = '' 
    primeiro = 0
    while primeiro < len(frase):
        if frase[primeiro] not in 'AEIOUaeiou':
            str.upper(frase[primeiro])
            frase1 = frase
        primeiro = primeiro +1 
    return frase