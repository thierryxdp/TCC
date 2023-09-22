def lingua_p(palavra):
    a='AEIOUaeiou'
    i=0
    
    c=()
    for x in range(len(palavra)):
        if palavra[i] in a:
            c.append([i]+'p'+b[i])
    i+=1
	return c