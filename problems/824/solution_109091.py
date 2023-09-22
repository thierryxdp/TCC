def uppCons(frase):
    cons = "qwrtypsdfghjklçzxvnm"
    indice = 0
    while indice < len(frase):
        if cons in frase:
          d =  str.replace(frase,cons,str.upper(cons))
    return d
		indice =+ 1