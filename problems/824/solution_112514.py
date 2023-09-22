def uppCons (frase):
    """Retorna uma frase com todas as consoantes da frase dada como entrada
    em letra maiúscula. str-> str"""
    i = 0
    uppercons = ''
    while i < len(frase):
        if frase[i] in'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            uppercons = uppercons + str.upper(frase[i])
        else:
            uppercons = uppercons + str(frase[i])
        i = i+1
    return uppercons