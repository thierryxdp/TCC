def hashtag(s):
    l = list(s)
	l[0] = '#'
    l[-1] = '#'
    l[(len(s)//2)] = '#'
	s = "".join(l)
    return s