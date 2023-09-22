def conta_frases(x):
    k = []
    
    if x.count("...")>0:
    	k =len(k[0]) + x.count("...")
    if x.count("!")>0:
    	k =len(k[1]) + x.count("!")
    if x.count("?")>0:
    	k =len(k[2]) + x.count("?")
    if x.count(".")>0:
    	k =len(k[3]) + x.count(".")
    return k