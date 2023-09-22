def conta_frases(string):
	final=0
    for x in range(len(string)):
        if string[x]=="." and string[x-1]!=x and x!=0:
            final+=1
    
    
    
    excl=string.count("! ")
    inter=string.count("? ")
    ret=string.count("... ")
    return final+excl+inter+ret+1