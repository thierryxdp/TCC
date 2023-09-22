def hashtag(frase):
    total = 0
    for i in frase:
        total = total + 1
		z = '#'
    if (total % 2) == 0:
        x = (total/2)
        primeira_metade = frase[:int(x)]
        segunda_metade = frase[int(x):]
        re = z + primeira_metade + z + segunda_metade +z
		return re
	elif (total == 0):
        return '###'
    else:   
        x = (total/2)
        y = (total/2)
        primeira_metade = frase[:int(x)]
        segunda_metade = frase[int(y):]
        ge = z + primeira_metade + z + segunda_metade + z
		return ge