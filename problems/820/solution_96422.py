def posLetra(s, l, num):
    pos = 0
    if str.count(s, l) < num:
        return -1
    else:
        while num >= 1:
            pos = str.find(s, l, pos) + 1
            num = num - 1
    	return pos - 1