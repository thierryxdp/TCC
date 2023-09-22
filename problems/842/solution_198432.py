def pontos_por_time(cv, ce, cs, fv, fe, fs):
    
    if (cv*3 + ce*1) > (fv*3 + fe*1):
        return 'Cormengo'
    
    elif (fv*3 + fe*1) > (cv*3 + ce*1):
        return 'Flaminthians'

    elif (fv*3 + fe*1) == (cv*3 + ce*1):
        if cs > fs:
            return 'Cormengo'
        elif fs > cs:
            return 'Flaminthians'
        else:
            return 'Empate'