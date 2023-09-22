def uppCons(s):
    r = ""
    for x in s:
        if x not in ("a","á","e","é","i","í","o","ó","u","ú"):
            r+=str.upper(x)
        else:
            r+=(x)
    return r