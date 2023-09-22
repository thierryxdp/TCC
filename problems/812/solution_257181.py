def retira_pontuacao(x):
    w = ""
    w = x.replace("."," ")
    w = x.replace("!"," ")
    w = x.replace("?"," ")
    w = x.replace(","," ")
    w = x.replace("-"," ")
    w = x.replace(":"," ")
    w = x.replace(";"," ")
    if w.count(".")>0 or w.count("!")>0 or w.count("?")>0 or w.count(",")>0 or w.count(":")>0 or w.count("-")>0 or w.count(";"):
    	return w