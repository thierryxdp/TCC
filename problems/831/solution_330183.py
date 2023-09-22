def lingua_p(palavra):
    str.lower(palavra)
    x = 0
    y = 0
    for vogal in palavra:
        if vogal in 'AEIOUaeiou':
            y = y + palavra[x]
            x = x + 1