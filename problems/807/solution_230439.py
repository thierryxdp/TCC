def conta_frases(s):
    return str.replace(s,"...","+")
    ls=str.count(s,"+")+str.count(s,"!")+str.count(s,"?")