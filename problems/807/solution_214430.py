def conta_frases(s) :
    s = s.replace("!",".").replace("?",".").replace("...",".")
    return str.count(s,".")