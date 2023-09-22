def filtra_pares(s):
    if s[:4] % 2 == 0:
        return s
    elif s[:3] % 2 == 0:
        return s[:3]
    elif s[:2] % 2 == 0:
        return s[:2]
    elif s[:1] % 2 == 0:
        return s[:1]
    elif s[0] % 2 == 0:
        return s[0]
    elif (s[0] % 2 == 0) + (s[2] % 2 == 0):
        return s[0] + s[2]
    elif (s[0] % 2 == 0) + (s[3] % 2 == 0):
        return s[0] + s[3]
    elif (s[0] % 2 == 0) + (s[4] % 2 == 0):
        return s[0] + s[4]
    elif (s[1] % 2 == 0) + (s[2] % 2 == 0):
        return s[1] + s[2]
    elif (s[1] % 2 == 0) + (s[3] % 2 == 0):
        return s[1] + s[3]
    elif (s[1] % 2 == 0) + (s[4] % 2 == 0):
        return s[1] + s[4]
    elif (s[2] % 2 == 0) + (s[3] % 2 == 0):
        return s[2] + s[3]
    elif (s[2] % 2 == 0) + (s[4] % 2 == 0):
        return s[2] + s[4]
    elif (s[3] % 2 == 0) + (s[4] % 2 == 0):
        return s[3] + s[4]
    elif s[4] % 2 == 0:
        return s[4]
    elif s[3] % 2 == 0:
        return s[3]
    elif s[2] % 2 == 0:
        return s[2]
    elif s[1] % 2 == 0:
        return s[1]
    else:
        return 'não contem numero par'