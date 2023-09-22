def lingua_p(palavra):
    for c in palavra:
        if c in 'aeiou':
            palavra+='p'
    return palavra