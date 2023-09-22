def primo(n):
	'''Função que recebe um número e retorna True se for um número primo e False
    caso contrário; int -> bool'''
    for i in range(2,n):
        if n % i == 0:
            return True
        else:
            return False