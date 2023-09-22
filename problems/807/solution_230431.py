def conta_frases(s):
    ls=str.count(s,'...')+str.count(s,"!")+str.count(s,"?")
    if("..." in s):
		return str.count(str.replace(s,"...","XXX"),"XXX")
    
    return ls+str.count(s,".")