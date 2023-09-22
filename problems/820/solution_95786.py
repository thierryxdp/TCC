def posLetra (string, letra, num):
    
    
    
    if num > str.count(string, letra):
        return '-1'
    cont, oco = 1, str.index(string,letra)
    while cont < num:
        cont +=1
        oco = str.index(string[oco +1:], letra)+ len(string[:oco+1])
	return oco