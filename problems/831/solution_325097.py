def ligua_p(palavra):
    for n in len(palavra):
        if palavra[n] in ['a','e','i','o','u','A','E','I','O','U']:
            palavra.replace(palavra[n], palavra[n]+'p')
    return palavra