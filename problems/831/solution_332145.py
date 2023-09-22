def lingua_p(palavra):
	p=''
    for i in palavra:
        if 'aeiouAEIOU'==palavra[i]:
            p=p+'p'+palavra[i]
        return p