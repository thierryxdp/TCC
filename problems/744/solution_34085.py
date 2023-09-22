def hashtag():
    frase = input("insira seu texto: ")
    total = 0
    for i in frase:
        total = total + 1
    if (total % 2) == 0:
        x = (total/2)
        primeira_metade = frase[:int(x)]
        segunda_metade = frase[int(x):]
        re = ("#",primeira_metade,"#",segunda_metade,"#")
		return re
    else:   
        x = (total/2)+1
        y = (total/2)+1
        primeira_metade = frase[:int(x)]
        segunda_metade = frase[int(y):]
        ge = ("#",primeira_metade,"#",segunda_metade,"#")
		return ge