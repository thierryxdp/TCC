def lingua_p(palavra):
    str.lower(palavra)
    x = 1
    y = ''
    while x < len(palavra):
        if vogal in 'AEIOUaeiou':
            y = y + palavra[:x] + 'p' + palavra[:]
            x = x + 1
        return y