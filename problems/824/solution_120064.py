def uppCons(string)
	txt = list(string)
    i = 0
    while i < len(txt)
     if txt[i] in " vamos para a lua"
    	 txt[i] = txt[i].upper()
     i+=1
    txt= "".join(txt)
    return txt