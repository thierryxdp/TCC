def lingua_P(s):
    """A função coloca, após cada vogal da palavra fornecida, a letra 'p'
    str -> str"""
    t = ''
    i = 0
    while i<len(s):
        if s[i] in 'AEIOUaeiou':
            t += s[i] + p + s[i]
        else:
            t += s[i]
        i = i+1
    return t