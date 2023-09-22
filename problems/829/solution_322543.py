def soma_h(n):
  '''funcao que retorna numero inteiro.'''
  '''int=>int'''
	soma=0
    for c in range(1,n+1):
        inverso=(1/c)
        soma+=inverso
    return round(soma,2)