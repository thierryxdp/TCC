def primo(n):
    qtd=1
    for i in range(1,n//2+1):
	if n%i==0:
            qtd+=1
	if qtd==2:
            return True
    else:
            return False