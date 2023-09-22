def conta_frases(x):
    if x.count(".")>=0:
    	qnt = x.count(".")
    if x.count("!"):
    	qnt = x.count("!")
    if x.count("?"):
    	qnt = x.count("?")
    if x.count("..."):
    	qnt = x.count("...")
    return qnt