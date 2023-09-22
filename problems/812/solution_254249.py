def retira_pontuacão(texto):
    if  (',' in texto)==True:
        t=str.replace(texto, ',', '')
        if ('.' in t)== True:
            return str.replace(t, '.', '')
                    
        if ('?' in t)==True:
            return str.replace(texto, '?', '')
                      
                        
        if ('!' in t)==True:
            return str.replace(texto, '!', '')
            
    if  ('.' in texto)==True:
        t=str.replace(texto, ',', '')
        if (',' in t)== True:
            return str.replace(t, ',', '')
            
        if ('?' in t)==True:
            return str.replace(texto, '?', '')
                      
                        
        if ('!' in t)==True:
            return str.replace(texto, '!', '')

    if  ('?' in texto)==True:
        t=str.replace(texto, '?', '')
        if (',' in t)== True:
            return str.replace(t, ',', '')
            
        if ('.' in t)==True:
            return str.replace(texto, '.', '')
                      
                        
        if ('!' in t)==True:
            return str.replace(texto, '!', '')

    if  ('!' in texto)==True:
        t=str.replace(texto, '!', '')
        if (',' in t)== True:
            return str.replace(t, ',', '')
            
        if ('.' in t)==True:
            return str.replace(texto, '.', '')
                      
                        
        if ('?' in t)==True:
            return str.replace(texto, '?', '')