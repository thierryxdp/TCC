def conta_frases(x):
    if x.count("...")>0:
    	k =k + x.count("...")
    if x.count("!")>0:
    	k =k + x.count("!")
    if x.count("?")>0:
    	k =k + x.count("?")
    if x.count(".")>0:
    	k =k + x.count(".")
    return k