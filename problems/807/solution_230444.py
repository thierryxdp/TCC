def conta_frases(s):
    if("..." in s):
    	return str.replace(s,"...","+")
    	ls=str.count(s,"+")+str.count(s,"!")+str.count(s,"?")
    
    	if("+" in s):
        	return ls+str.count(s,".")
    return 0