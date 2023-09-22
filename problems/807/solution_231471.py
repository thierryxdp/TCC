def conta_frases(frase):
	final1 = str.count(frase, .)
   	final2 = str.count(frase, !)
   	final3 = str.count(frase, ?)
   	final4 = str.count(frase, ...)
   	resultado = final1+final2+final3+final4
return resultado