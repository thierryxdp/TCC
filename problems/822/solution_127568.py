def repetidos(lista):
    i=0
    
    while i<len(lista):
        if i==0:
        	x=list.count(lista,i)
  	     	y=x
            i+=1
        else:
            x=list.count(lista,i)
            if x>y:
                y=x
        return y