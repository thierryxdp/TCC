def inverte(far, oi=0):
    oi = str.replace(str.replace(str.replace(str.replace(str.replace(far, '.', ' '), ',', ' '), '!', ' '), '?', ' '), '-', ' ')
    return str.split(oi)[-1::-1][0] + ' ' + str.split(oi)[-1::-1][1] + str.split(oi)[-1::-1][2] + str.split(oi)[-1::-1][3] + str.split(oi)[-1::-1][4] + str.split(oi)[-1::-1][5] + str.split(oi)[-1::-1][6] + str.split(oi)[-1::-1][7]