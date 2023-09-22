def media (matriz):
	x = 0
    y = 0
    z = 0
    
	while x < len(matriz):
        for i in matriz[x]:
            y =  y + i
            z = z + 1
		x += 1
    return round(y/z)