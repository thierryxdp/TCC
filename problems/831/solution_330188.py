def lingua_p(palavra):
    str.lower(palavra)
    x = 1
    y = ''
    while x < len(palavra):
        if palavra[x] in 'aeiou':
            y = y + palavra[:x] + 'p' + palavra[:]
            x = x + 1
        return y