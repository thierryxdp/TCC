def lingua_p(palavra):
    a='AEIOUaeiou'
    i=0
    b=palavra.split()
    for x in range(len(palavra)):
        if b[i] in a:
            b[i]=(b[i]+'p'+b[i])
    i+=1
	return b