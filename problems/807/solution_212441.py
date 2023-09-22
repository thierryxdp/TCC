def conta_frases(texto):
    
    if (('...' in texto)== True):
        t=str.split(texto,'...')
        if (('!' in texto)== True):
            e=str.split(texto,'!')
            if (('?' in texto)== True):
                x=str.split(texto,'?')
                if (('.' in texto)==True):
                    o=str.split(texto,'.')
                    return int(len(t)) + int(len(e)) + int(len(x)) + int(len(o)) - 3 - (int(len(t))//2)*4
        if (('.' in texto)==True):
            e=str.split(texto,'.')
            return int(len(t)) - 2 + int(len(e))//3
    
    if (('.' in texto)== True):
        t=str.split(texto,'.')
        if (('!' in texto)== True):
            e=str.split(texto,'!')
            if (('?' in texto)== True):
                x=str.split(texto,'?')
                return int(len(t)) + int(len(e)) + int(len(x)) - 3
            else:
                return int(len(t)) + int(len(e))-2
        if (('?' in texto)==True):
            e=str.split(texto,'?'),
            return int(len(t))-1 + len(e)
        else:
            return int(len(t)) -1
            

    if (('?' in texto)== True):
        e=str.split(texto,'?')
        return len(e) -1
    else:
        return len([texto])