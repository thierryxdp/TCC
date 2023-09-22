def posLetra(s, l, i):
    if s.count(l) <= i:
    	return s.find(l, i)
    return -1