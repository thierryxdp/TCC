def lingua_p(s):
    x=''
    i=0
    while i<len(s):
        a= (s[i].lower())
        if s[i] in 'AEIOUaeiouÁÉÍÓÚáéíóúÀÈÌÒÙàèìòùÃÕãõÂÊÔâêô':
            x+=a+'p'+a
        else:
            x+=a
        i+=1
        return x