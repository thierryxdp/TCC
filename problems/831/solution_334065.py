def lingua_p(a):
    b = ''
    for i in range(len(a)):
        if a[i] in 'AEIOUaeiou':
            b = b + a[i] + 'p'
		else:
            b = b + a[i]
	return str.lower(b)