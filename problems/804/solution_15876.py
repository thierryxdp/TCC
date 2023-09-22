def filtra_pares(nuemros):
        """retorna somente os pares de uma dada tupla de quatro elementos.
    entra sequencia de quatro numeros(numeros);tupla(int,int,int,int)->
    tupla(int) a quantidade de elementos da tupla final depende da quantidade
    de pares da tupla inicial"""
	tuplafinal=()
	w=numeros[0]
	x=numeros[1]
	y=numeros[2]
	z=numeros[3]
	if w%2==0:
	  tuplafinal=(w,)
	if x%2==0:
          tuplafinal1=(x,)
          tuplafinal=(tuplafinal+tuplafinal1)
	if y%2==0:
	 tuplafinal2=(y,)
	 tuplafinal=(tuplafinal+tuplafinal2)
	if z%2==0:
	 tuplafinal3=(z,)
	 tuplafinal=(tuplafinal+tuplafinal3)
	 return tuplafinal