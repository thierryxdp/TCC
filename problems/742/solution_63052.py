def substitui(s, x, i):
	if i >= 0 and i < len(s) - 1:
		s=list(s)
		s[i] = x
		s = "".join(s)
	return s