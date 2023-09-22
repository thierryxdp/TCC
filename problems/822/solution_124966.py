def repetidos (listaN):
    i=0
    res=[]
    while i<len(listaN):
        if listaN[i]<listaN[(i-1)]:
        	res=res+listaN[i]  
    i=i+1
    return len(res)