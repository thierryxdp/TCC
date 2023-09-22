def inverte(txt):
    y = txt.replace('-',' ')
    y = y.replace(',',' ')
    y = y.replace(':',' ')
    y = y.replace(';',' ')
    y = y.replace('.',' ')
    y = y.replace('!',' ')
    y = y.replace('?',' ')
    x = y.split(' ')
    if x[0] == ' ':
        x = x.replace(' ','')
    if len(x) == 9:
        return str(x[-1]+ ' '+x[-2]+ ' '+x[-3]+ ' '+x[-4]+ ' '+x[-5]+ ' '+x[-6]+ ' '+x[-7]+ ' '+x[-8]+ ' '+x[-9])
    elif len(x) == 8:
        return str(x[-1]+ ' '+x[-2]+ ' '+x[-3]+ ' '+x[-4]+ ' '+x[-5]+ ' '+x[-6]+ ' '+x[-7]+ ' '+x[-8])
    elif len(x) == 7:
        return str(x[-1]+ ' '+x[-2]+ ' '+x[-3]+ ' '+x[-4]+ ' '+x[-5]+ ' '+x[-6]+ ' '+x[-7])
    elif len(x) == 6:
        return str(x[-1]+ ' '+x[-2]+ ' '+x[-3]+ ' '+x[-4]+ ' '+x[-5]+ ' '+x[-6])
    elif len(x) == 5:
        return str(x[-1]+ ' '+x[-2]+ ' '+x[-3]+ ' '+x[-4]+ ' '+x[-5])
    elif len(x) == 4:
        return str(x[-1]+ ' '+x[-2]+ ' '+x[-3]+ ' '+x[-4])
    elif len(x) == 3:
        return str(x[-1]+ ' '+x[-2]+ ' '+x[-3])
    elif len(x) == 2:
        return str(x[-1]+ ' '+x[-2])
    elif len(x) == 11:
        return str(x[-1]+ ' '+x[-2]+ ' '+x[-3]+ ' '+x[-4]+ ' '+x[-5]+ ' '+x[-6]+ ' '+x[-7]+ ' '+x[-8]+ ' '+x[-9]+ ' '+x[-10]+ ' '+x[-11])