def retira_pontuacao(texto):
    if(',' in texto)==True:
        t=str.replace(texto, ',', '')
        if ('.' in t)== True:
            return str.replace(t, '.', '')            
        if ('?' in t)==True:
            return str.replace(texto, '?', '')                       
        if ('!' in t)==True:
            return str.replace(texto, '!', '')
        else:
            return str.replace(texto, ',', '')
            
    elif('.' in texto)==True:
        t=str.replace(texto, '.', '')
        if (',' in t)== True:
            return str.replace(t, ',', '')            
        if ('?' in t)==True:
            return str.replace(texto, '?', '')                                              
        if ('!' in t)==True:
            return str.replace(texto, '!', '')
        else:
            return str.replace(texto, '.', '')

    elif('?' in texto)==True:
        t=str.replace(texto, '?', '')
        if (',' in t)== True:
            return str.replace(t, ',', '')            
        if ('.' in t)==True:
            return str.replace(texto, '.', '')                                              
        if ('!' in t)==True:
            return str.replace(texto, '!', '')
        else:
            print str.replace(texto, '?', '')

    elif('!' in texto)==True:
        t=str.replace(texto, '!', '')
        if (',' in t)== True:
            return str.replace(t, ',', '')            
        if ('.' in t)==True:
            return str.replace(texto, '.', '')                                              
        if ('?' in t)==True:
            return str.replace(texto, '?', '')
        else:
            return str.replace(texto, '!', '')