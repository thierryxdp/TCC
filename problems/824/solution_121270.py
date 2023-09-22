def uppCons(frase):
    a=""
    for i in frase:
        if i not in 'aáãâàeéèêiìíîoòóõôuúùû':
            a+= str.upper(i)
        else:
             if i in 'aáãâàeéèêiìíîoòóõôuúùû':
                 a+= i
    return a