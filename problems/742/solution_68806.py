def substitui(s, x, i):
	
    sf = s[0:i] + str(x) + s[i+1:len(s)]

    return sf

    s = input("s: ")
    x = input("x: ")
    i = int(input("i: "))