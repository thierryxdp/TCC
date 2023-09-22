def uppCons(F):
    """Temos a string "F" na qual é modifica para que as suas consoantes fiquem maiúsculas
    str --> str"""
    F = str.upper(F)
    i = F[0:1]
    e = F[1:]
    
	r = ""
    for letras in e:
        if letras == "A":
            r = r + "a"
        elif letras == "E":
            r = r + "e"
        elif letras == "I":
            r = r + "i"
        elif letras == "O":
            r = r + "o"
        elif letras == "U":
            r = r + "u"
        elif letras == "Ã":
            r = r + "ã"
        elif letras == "Ó":
            r = r + "ó"
        elif letras == "Ó":
            r = r + "ó"
        elif letras == "Ú":
            r = r + "ú"
        elif letras == "Í":
            r = r + "í"
        elif letras == "É":
            r = r + "é"
		else:
            r = r + letras
	return i + r