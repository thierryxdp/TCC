def faltante(L):
   	posicao = i = x = 0
   	n = 1
    tamanho=len(L)
  	while i < tamanho + 1 :
      	if L[posicao] != n:
        	return n
      	else:
     		i += 1
       		n += 1