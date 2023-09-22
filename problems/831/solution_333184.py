def lingua_p(p):
    p = ''
    for i in p:
		if i.lower() in 'aeiou':
            p += i + 'p' + i
        else:
            p += i
	return p