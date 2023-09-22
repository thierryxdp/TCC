def uppCons (frase):
    """Retorna uma frase com todas as consoantes da frase dada como entrada
    em letra maiúscula. str-> str"""
    i = 0
    uppercons = ''
    while i < len(frase):
        if frase[i] not in'AEIOUaeiou':
            uppercons = uppercons + str.upper(frase[i])
        i = i+1
    return uppercons