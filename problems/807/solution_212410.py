def conta_frases(texto):
    if (('.' in texto)== True):
        t=str.split(texto,'.')
        if (('!' in texto)== True):
            e=str.split(texto,'!')
            if (('?' in texto)== True):
            x=str.split(texto,'?')
            
            return int(len(t)) + int(len(e)) + int(len(x)) - 3
            else:
                return int(len(t)) + int(len(e))-2           
        else:
            return int(len(t)) - 1

        if (('?' in texto)== True):
            e=str.split(texto,'?')
            return int(len(t)) + int(len(e))-2
        else:
            return int(len(t)) - 1