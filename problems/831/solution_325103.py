def lingua_p(palavra):
    for n in range(len(palavra)):
        if palavra[n] in ['a','e','i','o','u','A','E','I','O','U']:
            palavra = palavra.replace(palavra[n], palavra[n]+'p'+palavra[n])
            n = n + 3
    return palavra