def substitui(s, x, i):
	""" A função retorna uma string que tem um elemento
    escolhido, modificado por um caractere X """
    sf = s[0:i] + str(x) + s[i+1:len(s)]

    return sf

    s = input("s: ")
    x = input("x: ")
    i = int(input("i: "))