def lingua_p(palavra):
    """função que retorna a palavra em português traduzida para a língua do P
    str -> str"""
    palavra = str.lower(palavra)
    palavra = list(palavra)
    i = len(palavra) - 1
    while i >= 0 :
        if palavra[i] not in 'bcdfghjklmnpqrstvwxytz ':
            palavra[i+1:i+1]= 'p' + palavra[i]
        i -= 1
    return ''.join(palavra)