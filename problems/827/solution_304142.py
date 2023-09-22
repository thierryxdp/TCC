def qtd_divisores(n):
    div = 0
    for i in range(1,n+1):
        if not n%i:
            div+=1
  	return div