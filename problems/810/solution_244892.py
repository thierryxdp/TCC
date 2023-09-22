def inverte(x):
    if '.' in x:
        x=str.replace(x,'.',' ')
    if ',' in x:
        x=str.replace(x,',',' ')
    if ':' in x:
        x=str.replace(x,':',' ')
    if ';' in x:
        x=str.replace(x,';',' ')
    if '-' in x:
        x=str.replace(x,'-',' ')
    if '?' in x:
        x=str.replace(x,'?',' ')
    if '!' in x:
        x=str.replace(x,'!',' ')
    y= str.split(x,)
    z= y[::-1]
    a= str.join(z)
    return a