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
    return str.split(x)