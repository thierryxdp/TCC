def conta_frases(x):
    qnt = []
    if len(x.split(".",-1)) >=0:
    	qnt = len(x.split(".",-1)) + qnt
    if len(x.split("...",-1)) >=0:
    	qnt = len(x.split("...",-1))  + qnt 
    if len(x.split("!",-1)) >=0:
    	qnt = len(x.split("!",-1)) + qnt
    if len(x.split("?",-1))>=0:
    	qnt = len(x.split("?",-1)) + qnt               
    return qnt