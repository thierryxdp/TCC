def inverte(texto):
    if ((',' in texto)== True):
        t=str.replace(texto,',',' ')
        if (('-' in texto)== True):
            t=str.replace(texto,'-',' ')
            if (('.' in texto)== True):
                t=str.replace(texto,'.',' ')
                e=str.split(t)
                x=e[::-1]
                return str.join(' ',x)
        if (('.' in texto)== True):
                t=str.replace(texto,'.',' ')
                e=str.split(t)
                x=e[::-1]
                return str.join(' ',x)
        if (('?' in texto)== True):
                t=str.replace(texto,'?',' ')
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