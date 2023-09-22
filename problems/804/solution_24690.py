def pares(t)
	nova=(,)
    if t[0:1]%2==0:
        return nova+t[0:1]
    else:
        if t[1:2]%2==0:
            return nova+t[1:2]