def posLetra(string, letra, num):
    txt = list(string)
    i=0
    pos=[]
    while i < len(txt):
    	if txt[i].lower() == letra.lower():
               pos.append(i)
        i+=1
    	if len(pos) < num:
        	return -1
    	else:
    		return pos[num-1]