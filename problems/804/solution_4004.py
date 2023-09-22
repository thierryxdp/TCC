def formato_data(data):
    '''Retorna os possıveis formatos em que a data fornecida possa ser interpretada.'''
    aa = int(data[0:2])
    bb = int(data[3:5])
    cc = int(data[6:8])
    
    if 0<aa<=12 and 0<bb<=12 and 0<cc<=31:
        return ('dd/mm/yy' , 'yy/mm/dd' , 'mm/dd/yy' )
    elif 0<aa<=12 and 0<bb<=12 and cc>=0:
        return ('dd/mm/yy' , 'mm/dd/yy')
    elif 0<aa<=31 and 0<bb<=12 and 0<cc<=31:
        return ('dd/mm/yy' , 'yy/mm/dd')
    elif aa>=31 and 0<bb<=12 and 0<cc<=31:
        return ('yy/mm/dd')
    elif 12<aa<=31 and 0<bb<=12 and cc>31:
        return ('dd/mm/yy')
    elif 0<aa<=12 and bb>12 and cc>0:
        return ('mm/dd/yy')
    else:
        return '()'