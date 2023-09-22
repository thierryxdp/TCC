def conta_frases(s):
    total=0 
    if(str.count(s,".")>0):
        total=str.count(s,".")
    if(str.count(s,"...")>0):
        total+=str.count(s,".")
    if(str.count(s,"!")>0):
        total+=str.count(s,".")
    if(str.count(s,"?")>0):
        total+=str.count(s,".")
    return total