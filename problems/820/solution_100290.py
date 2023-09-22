def posLetra (s,letra,num):
	posicao = s.find(letra)
    while posicao >= 0 and num > 1 :
	        posicao = s.find(letra, posicao + 1)
    		num=num-1
	return posicao
'''dado uma frase, uma letra e um numero, retorna 
a posicao da letra na frase, de acordo com a 
ocorrencia definida pelo numero
str,str,int->int'''