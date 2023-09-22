def inverte(far, oi=0):
    oi = str.replace(str.replace(str.replace(str.replace(str.replace(far, '.', ' '), ',', ' '), '!', ' '), '?', ' '), '-', ' ')
    if len(str.split(oi)) == 3:
        return str.lower(str.split(oi)[-1::-1][0] + ' ' + str.split(oi)[-1::-1][1] + ' ' + str.split(oi)[-1::-1][2] + ' ' + str.split(oi)[-1::-1][3]