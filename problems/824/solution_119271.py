def uppCons(frase):

    FM = frase.upper()

    f1 = FM.replace("A","a")
    f2 = f1.replace("E","e")
    f3 = f2.replace("I","i")
    f4 = f3.replace("O","o")
    f5 = f4.replace("U","u")
	
    return f5