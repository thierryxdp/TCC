def conta_frases(F):
    x0 = F.replace('. ',"','")
    x1 = x0.replace('! ',"','")
    x2 = x1.replace('? ',"','")
    x3 = x2.repalce('...',"")
    return len(x3)