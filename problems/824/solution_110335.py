def uppCons(frase):
    """ Essa função recebe uma frase e retorna todas as con
    soantes em letra maiúsculas. str->str."""
    frase1 = '' 
    primeiro = 0
    vogal = ' ' 
    while primeiro < len(frase):
        if frase[primeiro] in 'AEIOUaeiou':
            vogal = frase[primeiro]
            frase1 = frase1 + frase + str.upper(vogal)
        primeiro = primeiro +1 
    return frase1