def uppCons(s):
    i = 0
    while i < len(s):
        if s[i] != 'AEIOUaeiou':
            s.replace(s[i], s[i].upper())
            return s
        i = i + 1