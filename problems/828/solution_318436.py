def primo(n):
    from math import ceil
    NDivs=0
    for i in range(ceil(n/2)):
    	if n==2:
            return True
        elif i>0 and n%i==0 :
            NDivs+=1 
    if len(NDivs)==2:
        return True
    else:
        return False