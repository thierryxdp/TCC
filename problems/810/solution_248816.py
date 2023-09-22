def inverte (x:str):
    if '.'or'!'or'?'or'-'or','or';'or':' in x:
        str.split(str.lower(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(x,'.',' '),'!',' '),'?',' '),'-',' '),',',' '),':',' '),';',' ')))
        return x
    else:
        return str.lower(x)