def uppCons(frase):
    """recebe uma string e retorna-a com todas as suas consoantes minúsculas substituídas por consoantes maiúsculas
    str->str"""
    for x in frase:
        if x in ["a","e","i","o","u","á","é","í","ó","ú","à","è","ì","ò","ù","â","ê","î","ô","û","ã","õ"]:
            r+=x
        else:
            r+=str.upper(x)
    return r