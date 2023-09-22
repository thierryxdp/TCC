def primo(numero):
    '''dado um numero inteiro positivo, verifica se este é primo ou nao, retorna True para primo e False para nao primo; int -> bool'''
    quantidade = 0
    for divisor in range(1, numero+1):
        if numero%divisor == 0:
            quantidade += 1
    if quantidade == 2:
        return True 
    else:
        return False