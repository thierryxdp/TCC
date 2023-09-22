def inverte(s):
    char = ['!','?','.',',',';','-',':','...']
    s = str.replace(s,'.',' ')
    s = str.replace(s,'...',' ')
    s = str.replace(s,'!',' ')
    s = str.replace(s,'?',' ')
    s = str.replace(s,'-',' ')
    s = str.replace(s,',',' ')
    s = str.replace(s,';',' ')
    s = str.replace(s,':',' ') 
    s=str.split(s)
    r=s[::-1]
    t=str.join(' ',r)
    return t.lower()