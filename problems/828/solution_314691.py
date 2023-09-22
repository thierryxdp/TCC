def divisores(n):
    divisores = []
    for i in range(1,n+1):
        if n%i == 0:
            list.append(divisores,i)
            i+=1
    return divisores

def primo(x):
    primos=[]
    i=1
    if len(divisores(x))== 2:
    	return True
    else:
    	return False