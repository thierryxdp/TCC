def faltante(L):
   	posicao = i = 0
   	n = 1
  	while i < (len(L) + 1):
            if L[posicao] != n:
                return n
            else:
                i += 1
                n += 1
                posicao += 1