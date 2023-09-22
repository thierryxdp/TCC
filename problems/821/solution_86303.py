def fatorial(n):
  """Fatorial 0 deve ser 1"""
  fatorial = 1
  """Se o número for maior que 0, será feito o cálculo"""
  if int(n) >= 1:
	for i in range(1, int(n) + 1):
    	fatorial = fatorial * i
    return fatorial