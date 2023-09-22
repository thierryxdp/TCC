def lingua_p(s):
    i=0
    k=""
    while i<len(s):
        if(s[i] in "aeiou"):
            k=k+s[i]+"p"
            i=i+1
        else:
            k=k+s[i]
            i=i+1
    return k