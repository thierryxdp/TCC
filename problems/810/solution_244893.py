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
    Lista= str.splt(x,)
    listainversa= Lista[::-1]
    aocontrario= str.join(listainversa,)