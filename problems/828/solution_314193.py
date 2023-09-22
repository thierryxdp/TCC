def primo(n):
    ''' Função que verifica se um numero é primo ou não
int -> bool'''
    conta = []
    for i in range(1, n+1):
        list.append(conta,n%i)
    restos = (list.count(conta,0))
    if restos == 2:
        return True
    else:
        return False