def uppCons(frase):
    contador = 0
    final = ""
    while contador < (len(frase)):
        if frase[contador] not in "AEIOUÁÉÍÓÚÃÕÂÊÔaeiouáéíóúãõâêô":
           	final = final + str.upper(frase[contador])
        else: 
          	final = final+(frase[contador]) 
       	contador += 1
    return final