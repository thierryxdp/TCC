def conta_frases(s):
    if(str.count(s,"!")>0):
        c = str.count(s,"!")
    if(str.count(s,"?")>0):
        total = c + str.count(s,"!")
    if(str.count(s,".")>0):
        total = total + str.count(s,"!")
    if(str.count(s,"...")>0):
        total =total + str.count(s,"!")
    	return total