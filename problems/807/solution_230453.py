def conta_frases(s):
    k=str.replace(s,"...","+")
    ls=str.count(k,"!")+str.count(k,"?")+str.count(k,".")+str.count(k,"+")
    return ls