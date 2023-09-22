'''Retorna o resultado do teste de primalidade de um numero n'''
#int -> bool
def primo(n):
    if n <= 0:
        return 'O numero n precisa ser positivo'
    else:
        for index in range(2, n):
            if n%index != 0:
                return True
            elif index == n - 1:
                return False