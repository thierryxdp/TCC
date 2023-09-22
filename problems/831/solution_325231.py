def lingua_p(palavra):
    s=0
    palavra.lower()
    for c in range(len(palavra)):
        if palavra[c] in 'aeiou':
            s=palavra[0:c]+'p'+palavra[c]+palavra[c:]
    return s