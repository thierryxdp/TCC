def lingua_p(palavra):
    a='AEIOUaeiou'
    i=0
    for x in range(len(palavra)):
        if palavra[i] in a:
            palavra[i]='b'
    i+=1
	return palavra[i]