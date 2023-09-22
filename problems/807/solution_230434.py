def conta_frases(s):
    str.replace(s,"...","XXX")
    ls=str.count(s,"XXX")+str.count(s,"!")+str.count(s,"?")+str.count(s,".")    
    return ls