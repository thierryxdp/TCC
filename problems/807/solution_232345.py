def conta_frases(string):
   			
	substring1 = "?"
    substring2 = "!"
    #substring3 = "."
    substring4 = "..."
    
	
	count1 = string.count(substring1)
    count2 = string.count(substring2)
    #count3 = string.count(substring3)
    count4 = string.count(substring4)

    count = count1 + count2 + count4
    
	return count