def inverte(far, oi=0):
    oi = str.replace(str.replace(str.replace(str.replace(str.replace(far, '.', ' '), ',', ' '), '!', ' '), '?', ' '), '-', ' ')
    if len(str.split(oi)) == 3:
        return str.lower(str.split(oi)[-1::-1][0] + ' ' + str.split(oi)[-1::-1][1] + ' ' + str.split(oi)[-1::-1][2])
    
    elif len(str.split(oi)) == 4:
        return str.lower(str.split(oi)[-1::-1][0] + ' ' + str.split(oi)[-1::-1][1] + ' ' + str.split(oi)[-1::-1][2] + ' ' + str.split(oi)[-1::-1][3])
    
    elif len(str.split(oi)) == 5:
        return str.lower(str.split(oi)[-1::-1][0] + ' ' + str.split(oi)[-1::-1][1] + ' ' + str.split(oi)[-1::-1][2] + ' ' + str.split(oi)[-1::-1][3] + ' ' + str.split(oi)[-1::-1][4])
                         
    elif len(str.split(oi)) == 6:
        return str.lower(str.split(oi)[-1::-1][0] + ' ' + str.split(oi)[-1::-1][1] + ' ' + str.split(oi)[-1::-1][2] + ' ' + str.split(oi)[-1::-1][3] + ' ' + str.split(oi)[-1::-1][4] + ' ' + str.split(oi)[-1::-1][5])
    
    elif len(str.split(oi)) == 8:
        return str.lower(str.split(oi)[-1::-1][0] + ' ' + str.split(oi)[-1::-1][1] + ' ' + str.split(oi)[-1::-1][2] + ' ' + str.split(oi)[-1::-1][3] + ' ' + str.split(oi)[-1::-1][4] + ' ' + str.split(oi)[-1::-1][5] + ' ' + str.split(oi)[-1::-1][6] + ' ' + str.split(oi)[-1::-1][7])
    
    elif len(str.split(oi)) == 9:
        return str.lower(str.split(oi)[-1::-1][0] + ' ' + str.split(oi)[-1::-1][1] + ' ' + str.split(oi)[-1::-1][2] + ' ' + str.split(oi)[-1::-1][3] + ' ' + str.split(oi)[-1::-1][4] + ' ' + str.split(oi)[-1::-1][5] + ' ' + str.split(oi)[-1::-1][6] + ' ' + str.split(oi)[-1::-1][7]+ ' ' + str.split(oi)[-1::-1][8])
    
    elif len(str.split(oi)) == 11:
        return str.lower(str.split(oi)[-1::-1][0] + ' ' + str.split(oi)[-1::-1][1] + ' ' + str.split(oi)[-1::-1][2] + ' ' + str.split(oi)[-1::-1][3] + ' ' + str.split(oi)[-1::-1][4] + ' ' + str.split(oi)[-1::-1][5] + ' ' + str.split(oi)[-1::-1][6] + ' ' + str.split(oi)[-1::-1][7]) + ' ' + str.split(oi)[-1::-1][8]) + ' ' + str.split(oi)[-1::-1][9]) + ' ' + str.split(oi)[-1::-1][11])