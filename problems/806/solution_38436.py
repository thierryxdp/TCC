def colisao(ret1,ret2):
	retangulo1_x = ret1[:1]
	retangulo1_y = ret1[2:3]
	retangulo1_width = ret1[4:5]
	retangulo1_height = ret1[6:7]
	retangulo2_x = ret2[0:1]
	retangulo2_y = ret2[2:3]
	retangulo2_width = ret2[4:5]
	retangulo2_height = ret2[6:7]
	if (retangulo1_x < retangulo2_x + retangulo2_width and
		retangulo1_x + retangulo2_width > retangulo2_x and
		retangulo1_y < retangulo2_y + retangulo2_height and
		retangulo1_y + retangulo1_height > retangulo2_y):
			return True
	else:
		return False