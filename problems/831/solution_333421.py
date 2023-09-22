def lingua_p(palavra):
    for x in palavra:
        if x == 'aeiou':
            x = x+'p'+x
    return palavra