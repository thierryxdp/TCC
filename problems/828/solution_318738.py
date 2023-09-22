def primo(x):
    if qtd_divisores(x) ==2:
        return True
	else:
        return False
def qtd_divisores(x):
    m=[]
    for e in range(x):
        if e!=0:
        	if x%e==0:
            	list.append(m,e)
    if len(m)==0:
        return len(m)
    else:
        return len(m)+1