'''Retorna o resultado do teste de primalidade de um numero n'''
#int -> bool
def primo(n):
    if n <= 0:
        return 'O numero n precisa ser positivo'
    else:
        contador = 0
        for index in range(2, n):
         	if n%index == 0:
                return False
       	return True