def lingua_p(palavra):
    palavra.lower()
    for c in len(palavra):
        if palavra[c] in 'aeiou':
            palavra[0:c]+'p'+palavra[c]+palavra[c:]
    return palavra