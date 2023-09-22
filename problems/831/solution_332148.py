def lingua_p(palavra):
	p=''
    for i in palavra:
        if 'aeiouAEIOU'==palavra:
            p=p+'p'+palavra
        return p