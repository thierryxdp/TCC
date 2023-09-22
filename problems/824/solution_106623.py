def uppCons(s):
    i = 0
    while i < len(s):
        if s[i] != 'AEIOUaeiou':
            s.replace(s[i], s[i].upper())
        i = i + 1
    return s