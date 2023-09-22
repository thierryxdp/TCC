def lingua_p(palavra):
    str.lower(palavra)
    x = 1
    y = ''
    for vogal in palavra:
        if vogal in 'AEIOUaeiou':
            y = y + palavra[:x] + 'p' + palavra[x:]
            x = x + 1
        return y