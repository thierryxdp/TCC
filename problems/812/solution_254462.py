def retira_pontuacao(texto):
    if('-' in texto)==True:
        t=str.replace(texto, '-', ' ')
        if (',' in t)== True:
            e= str.replace(t, ',', ' ')
            if('.' in e)==True:
                return str.replace(e,'.',' ')
        if ('.' in t)==True:
            return str.replace(t, '.', ' ')                                              
        if ('?' in t)==True:
            return str.replace(t, '?', ' ')
        if ('!' in t)==True:
            return str.replace(t, '!', ' ')
        else:
            return str.replace(t, '-', ' ')
        
    elif(',' in texto)==True:
        t=str.replace(texto, ',', ' ')
        if ('.' in t)== True:
            return str.replace(t, '.', ' ')            
        if ('?' in t)==True:
            return str.replace(t, '?', ' ')                       
        if ('!' in t)==True:
            return str.replace(t, '!', ' ')
        if ('-' in t)==True:
            e= str.replace(t, '-', ' ')
            if('.' in e)==True:
                return str.replace(e,'.',' ')
        else:
            return str.replace(t, ',', ' ')
        
            
    elif('.' in texto)==True:
        t=str.replace(texto, ',', ' ')
        if (',' in t)== True:
            return str.replace(t, ',', ' ')            
        if ('?' in t)==True:
            return str.replace(t, '?', ' ')                                              
        if ('!' in t)==True:
            return str.replace(t, '!', ' ')
        
        else:
            return str.replace(t, '.', ' ')

    elif('?' in texto)==True:
        t=str.replace(texto, '?', ' ')
        if (',' in t)== True:
            return str.replace(t, ',', ' ')            
        if ('.' in t)==True:
            return str.replace(t, '.', ' ')                                              
        if ('!' in t)==True:
            return str.replace(t, '!', ' ')
        if ('-' in t)==True:
            return str.replace(t, '-', ' ')
        else:
            return str.replace(t, '?', ' ')

    elif('!' in texto)==True:
        t=str.replace(texto, '!', ' ')
        if (',' in t)== True:
            return str.replace(t, ',', ' ')            
        if ('.' in t)==True:
            return str.replace(t, '.', ' ')                                              
        if ('?' in t)==True:
            return str.replace(t, '?', ' ')
        if ('-' in t)==True:
            return str.replace(t, '-', ' ')
        else:
            return str.replace(t, '!', ' ')