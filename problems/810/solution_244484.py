def inverte(y):
    x=str.lower(y,)
    if '.' in x:
        x=str.replace(x,'.','')
    if ',' in x:
        x=str.replace(x,',','')
    if ':' in x:
        x=str.replace(x,':','')
    if ';' in x:
        x=str.replace(x,';','')
    if '-' in x:
        x=str.replace(x,'-','')
    if '?' in x:
        x=str.replace(x,'?','')
    if '!' in x:
        x=str.replace(x,'!','')
    return x[:0:-1]