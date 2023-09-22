def inverte (x:str):
    if '.'or'!'or'?'or'-'or','or';'or':' in x:
        return str.lower(''.join(list.reverse(str.split(str.lower(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(x,'.',' '),'!',' '),'?',' '),'-',' '),',',' '),':',' '),';',' '))))))
    else:
        return str.lower(x)