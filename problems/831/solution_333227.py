def lingua_P(str):
    """A função coloca, após cada vogal da palavra fornecida, a letra 'p'
    str -> str"""
    t = ''
    i = 0
    while i<len(str):
        if s[i] in 'AEIOUaeiou':
            t += str[i] + 'p' + str[i]
        else:
            t += str[i]
        i = i+1
    return t