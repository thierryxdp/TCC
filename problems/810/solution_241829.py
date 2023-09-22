def inverte(txt):
    x = txt.replace('-',' ')
    x = x.replace(',',' ')
    x = x.replace(':',' ')
    x = x.replace(';',' ')
    x = x.replace('.',' ')
    x = x.replace('!',' ')
    x = x.replace('?',' ')
    y = x.split(' ')
    return str(y[-1]+' '+y[-2]+' '+y[-3]+' '+y[-4]+' '+y[-5]+' '+y[-6]+' '+