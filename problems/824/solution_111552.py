def uppCons(frase):
    y=0
    z='AEIOUÁÉÍÓÚÃÕÂÊÎÔÛaeiouáéíóúãõâêîôû'
    while y<len(frase):
        if frase[y] not in z:
            frase=frase.replace(frase[y],str.upper(frase[y]))
        y=y+1
    return frase