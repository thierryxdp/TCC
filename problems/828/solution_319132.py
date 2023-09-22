def primo(x):
'''Dado um numero inteiro, a funcao retorna um valor booleano que indica se este numero e primo ou nao
int -> bool'''
    for num in range(2,x):
        if x%num == 0:
            return False
    else:
        return True