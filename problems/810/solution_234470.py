def inverte(texto):
    texto=str.lower(texto)
    if ((',' in texto)== True):
        t=str.replace(texto,',',' ')
        if (('-' in t)== True):
            t=str.replace(t,'-',' ')
            if (('.' in t)== True):
                t=str.replace(t,'.',' ')
                e=str.split(t)
                x=e[::-1]
                return str.join(' ',x)
        if (('.' in texto)== True):
                t=str.replace(texto,'.',' ')
                e=str.split(t)
                x=e[::-1]
                return str.join(' ',x)
        if (('?' in t)== True):
                t=str.replace(t,'?',' ')
                e=str.split(t)
                x=e[::-1]
                return str.join(' ',x)
        if (('.' in t)== True):
                t=str.replace(t,'.',' ')
                e=str.split(t)
                x=e[::-1]
                return str.join(' ',x)
        
        
    if (('!' in texto)== True):
        t=str.replace(texto,'!',' ')
        e=str.split(t)
        x=e[::-1]
        return str.join(' ',x)
    
    if (('.' in texto)== True):
        t=str.replace(texto,'.',' ')
        
        e=str.split(t)
        x=e[::-1]
        return str.join(' ',x)
    
    if(('-' in texto)==True):
        t=str.replace(texto,'-',' ')
        e=str.split(t)
        x=e[::-1]
        return str.join(' ',x)