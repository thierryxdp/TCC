def lingua_p(palavra):
    palavra.lower()
    a = ''
    for c in range(len(palavra)):
        if palavra[c] in 'qwrtypsdfghjklçzxcvbnm':
            a+=palavra[c]
        else:
            a=a+palavra[c]+'p'+palavra[c]
    return a