def soma_h(n):
    """Retorna o valor da série H.
Assinatura: int --> int
Teste:
soma_h(2) == 1.5
soma_h(4) == 2.08
"""
    H = 1/n
    ls = []
 for x in range(1, n+1):
    	ls.append(1/x)
	 return round(sum(ls), 2)