def lingua_p(palavra):
    for i in palavra:
        if i in 'aeiou':
            i = 'ipi'
    return palavra