def uppCons(s):
    """Recebe uma string e retorna uma string consoante maiuscula, str-->str"""
    r = ""
    for x in s:
        if x not in ("a","á","ã","e","é","i","í","o","ó","õ","u","ú"):
            r+=str.upper(x)
        else:
            r+=(x)
    return r