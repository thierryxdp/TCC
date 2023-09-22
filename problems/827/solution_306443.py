def qtd_divisores(num):
    l=[1]
    for i in range(1, num//2+1):
	    if num % i == 0:
		    list.append(l,i)
    return len(l)