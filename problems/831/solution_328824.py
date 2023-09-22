def lingua_p(palavra):
    palavra=palavra.split()
    for i in palavra:
        if i in 'aeiuoAEIOU':
            n=list.index(palavra,i)
            list.insert(palavra,(n+1),'p')
    	return palavra