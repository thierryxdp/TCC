def conta_frases(texto):
    if  (',' in texto)==True:
        t=str.replace(texto, ',', '')
        if ('.' in t)== True:
            t=str.replace(t, '.', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')

        if (';' in t)==True:
            t=str.replace(texto, ';', '')
            if ('.' in t)==True:
                return str.replace(t, '.', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')
            
        if (':' in t)==True:
            t=str.replace(texto, ':', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if ('.' in t)==True:
                 return str.replace(t, '.', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')
            
        if ('-' in t)==True:
            t=str.replace(texto, '-', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('.' in t)==True:
                return str.replace(t, '.', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')
            
        if ('?' in t)==True:
            t=str.replace(texto, '?', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('.' in t)==True:
                return str.replace(t, '.', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')
            
        if ('...' in t)==True:
            t=str.replace(texto, '...', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('.' in t)==True:
                return str.replace(t, '.', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')
            
        if ('!' in t)==True:
            t=str.replace(texto, '!', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('.' in t)==True:
                return str.replace(t, '.', '')
    if  ('.' in texto)==True:
        t=str.replace(texto, '.', '')
        if (',' in t)== True:
            t=str.replace(t, ',', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')

        if (';' in t)==True:
            t=str.replace(texto, ';', '')
            if (',' in t)==True:
                return str.replace(t, ',', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')
            
        if (':' in t)==True:
            t=str.replace(texto, ':', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (',' in t)==True:
                 return str.replace(t, ',', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')
            
        if ('-' in t)==True:
            t=str.replace(texto, '-', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if (',' in t)==True:
                return str.replace(t, ',', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')
            
        if ('?' in t)==True:
            t=str.replace(texto, '?', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if (',' in t)==True:
                return str.replace(t, ',', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')
            
        if ('...' in t)==True:
            t=str.replace(texto, '...', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if (',' in t)==True:
                return str.replace(t, ',', '')
            if ('!' in t)==True:
                return str.replace(t, '!', '')
            
        if ('!' in t)==True:
            t=str.replace(texto, '!', '')
            if (';' in t)==True:
                return str.replace(t, ';', '')
            if (':' in t)==True:
                 return str.replace(t, ':', '')
            if ('-' in t)==True:
                return str.replace(t, '-', '')
            if ('?' in t)==True:
                return str.replace(t, '?', '')
            if ('...' in t)==True:
                return str.replace(t, '...', '')
            if (',' in t)==True:
                return str.replace(t, ',', '')