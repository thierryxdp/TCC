def primeiro(ls):
    return ls[-1:]

def resto(ls):
    return ls[1:]

def listavazia(ls):
    if ls == []:
        return []

def inverte(ls):
    return primeiro(ls), inverte(resto(ls))