def filtra_pares(s):
    '''dada uma tupla s, retorna uma nova tupla apenas com os números pares da tupla s;
    tupla(int,int,int,int)->tupla(int,int,int,int)'''
    a = s[0]
    b = s[1]
    c = s[2]
    d = s[3]
    
    if a%2==0:
        if b%2==0:
            if c%2==0:
                if d%2==0:
                    return s
                else:
                    return s[:3]
            else:
                if d%2==0:
                    return s[:2]+s[3:]
                else:
                    return s[:2]
        else:
            if c%2==0:
                if d%2==0:
                    return s[:1]+s[2:]
                else:
                    return s[:1]+s[2:3]
            else:
                if d%2==0:
                    return s[:1]+s[3:]
                else:
                    return s[0]
    else:
        if b%2==0:
            if c%2==0:
                if d%2==0:
                    return s[1:]
                else:
                    return s[1:3]
            else:
                if d%2==0:
                    return s[1:2]+s[3:]
                else:
                    return s[1]
        else:
            if c%2==0:
                if d%2==0:
                    return s[2:]
                else:
                    return s[2]
            else:
                if d%2==0:
                    return s[3]
                else:
                    return ''