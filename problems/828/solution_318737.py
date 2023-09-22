def primo(x):
    if qtd_divisores(x) == 2:
        return True
    else:
        return False
    
def qtd_divisores(x):
    j=[]
    for e in range(x):
        if e != 0:
            if x%e==0:
                list.append(j,e)
	if len(j) == 0:
        return len(j)
    else:
        return len(j) + 1