def uppCons(frase):
    """ Essa função recebe uma frase e retorna todas as con
    soantes em letra maiúsculas. str->str."""
    frase1 = '' 
    primeiro = 0
    while primeiro < len(frase):
        if frase[primeiro] in 'AEIOUaeiou':
            frase1 = frase1 + str.lower(frase[primeiro])
        primeiro = primeiro +1 
    return frase1