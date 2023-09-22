def faltante(lista):
   	contador=1
   	while contador<=len(lista)+1:
        if contador not in lista:
            return contador
        contador=contador+1