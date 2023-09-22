def lingua_p(s):
   i=0
	k=""
	while i<len(s):
   		if(s[i] in "aeiou"):
        	k=k+s[i]+"p"
        else:
            k=k+s[i]
    return k