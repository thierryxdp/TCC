def hashtag(s):
    i = 0
    r =''
    x = ((round((len(s)-1)/2)+1),0 )
    y =''
    while x < len(s):
        y = y + s[x]
        x = x + 1 
   
	while i < ((len(s)-1)/2):
        r = r + s[i]
    	i = i + 1
 
	return str('#') + r + str('#') + y + str('#')