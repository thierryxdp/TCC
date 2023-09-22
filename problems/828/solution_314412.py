def primo(n):
    qtd_divisores = 1
    for i in range(2,n):
        if not (n%i):
            return False
  	return True