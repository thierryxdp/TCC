def retira_pontuacao(s):
    if("-" in s): 
    	return str.replace(s,"-"," ")	
    if("," in s):
        return str.replace(s,","," ")
    if(":" in s):
        return str.replace(s,":"," ")
    if("." in s):
        return str.replace(s,"."," ")
    if(";" in s):
        return str.replace(s,";"," ")
    if("?" in s):
        return str.replace(s,'?"," ")
    if("!" in s):
        return str.replace(s,'?"," ")                   
    return []