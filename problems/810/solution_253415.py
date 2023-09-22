def inverte(f):
    n=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(f,'-',' '),':',' '),'?',' '),'!',' '),',',' '),'.',' ')
    s=str.lower(str.replace(str.replace(str.replace(n,'  ',' '),'  ',' '),'  ',' '))
    x=str.split(s)
    return str.join(' ',x[::-1])