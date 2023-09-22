def conta_frases(x):
    x=x.replace(',','')
    x=x.replace(' ','')
    x=x.replace('?',' ')
    x=x.replace('!',' ')
    x=x.replace('.',' ')
    x=x.replace('...',' ')
    x.split(' ',4)
    return len(x)