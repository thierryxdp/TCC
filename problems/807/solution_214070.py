def conta_frases(s):
    a=str.count(s,".")
    b=str.count(s,"!")
    c=str.count(s,"?")
    d=str.count(s,"...")
    return a or b or c or d