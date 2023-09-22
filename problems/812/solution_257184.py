def retira_pontuacao(x):
    w = ""
    if w.count(".")>0:
        w = x.replace("."," ")
        return w
    if w.count("!")>0:
        w = x.replace("!"," ")
        return w
    if w.count("?")>0:
        w = x.replace("?"," ")
        return w
    if w.count(",")>0:
        w = x.replace(","," ")
        return w
    if w.count(":")>0:
        w = x.replace(":"," ")
        return w
    if w.count("-")>0:
        w = x.replace("-"," ")
        return w
    if w.count(";")>0:
        w = x.replace(";"," ")
    	return w