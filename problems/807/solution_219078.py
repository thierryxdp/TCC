def conta_frases(s):
    char = ['.','!','?','...']
    if char[0] in s:
        sentences = str.count(s,char[0])
    	if char[1] in s:
        	sentences = sentences + str.count(s,char[1])
    		if char[2] in s:
        		sentences = sentences + str.count(s,char[2]) 
    			if char[3] in s:
        			sentences = sentences + str.count(s,char[3])
    return len(str(sentences))