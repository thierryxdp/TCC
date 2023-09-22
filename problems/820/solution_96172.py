def posLetra(palavra,x, y):
 	contador = 0
  	aparicao = 0
  	while (contador<len(palavra)):
     	for i in palavra:
          	if i == x:
             	aparicao = aparicao +1
             	if aparicao == y:
           	contador=contador+1
   
 	return