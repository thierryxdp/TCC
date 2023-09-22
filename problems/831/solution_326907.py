def lingua_p(palavra):
    c = 0
    nova_string = ''
    while c < len(palavra):
        if palavra[c] in 'aeiou':
            nova_string += palavra[c]+'p'+palavra[c]
        else:
            nova_string += palavra[c]
        c += 1
    return nova_string