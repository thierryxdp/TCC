def posLetra (string, letra, num):
    
    
    
    if num > str.count(string, letra):
        return '-1'
    cont, ind = 1, str.index(string,letra)
    while cont < num:
        cont +=1
        ind = str.index(string[ind +1:], letra)+ len(string[:ind+1])
	return ind