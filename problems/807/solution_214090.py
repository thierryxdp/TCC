def conta_frases(s):
    a=s.replace("!",".").replace("?".".").replace("...",".")
    return str.count(a,".")