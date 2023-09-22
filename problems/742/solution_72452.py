def substitui(s, x, i):
    s[i]=x
	s[0:i]+ x + s[i + 1:]
    return s