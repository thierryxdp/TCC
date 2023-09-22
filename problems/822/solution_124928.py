def repetidos (listaN):
    i=0
    res=[]
    while i<len(listaN):
        if listaN[i]==listaN[-1]:
        	res=res+listaN[i]  
    i=i+1
    return res