def conta_frases(s):
    a=str.count(s,".")
    b=str.count(s,"!")
    c=str.count(s,"?")
    d=str.count(s,"...")
    e=str.split(s)
    if str.endswith(e,"...")= True:
        return (a+b+c)-3
    else:
        return a+b+c