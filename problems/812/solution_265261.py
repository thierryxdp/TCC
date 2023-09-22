def retira_pontuacao(s):
    if(str.count(s,".")>0):
        v = str.replace(s,"."," ")
    	if(str.count(v,",")>0):
        	w = str.replace(v,","," ")
    		if(str.count(w,";")>0):
        		x = str.replace(w,";"," ")
    			if(str.count(x,"!")>0):
        			y = str.replace(x,"!"," ") 
    				if(str.count(y,"-")>0):
        				z = str.replace(y,"-"," ")
    				return z