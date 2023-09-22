def posLetra(tex, let, num):
    i = 0
    rep = 0
    posi = 0
    if(str.count(tex, let) > num):
   		while(i<len(tex) and rep<num):
     		if(tex[i] == let):
      	    	rep += 1
      	        i += 1
      	    else:
         	    i +=1
       return i
    
    else:
       return -1