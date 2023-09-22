def conta_frases(s):
    str.replace(s,"...","+")
    ls=str.count(s,"+")+str.count(s,"!")+str.count(s,"?")
    
    if("+" in s) and ("." in s):
        return ls+str.count(s,".")
    return 0