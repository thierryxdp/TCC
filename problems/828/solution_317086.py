def primo(numero):
    '''função que verifica se um dado número é primo ou não
    int -> bool'''
    contagem = 0
    for k in range(1,numero+1):
        if numero % k == 0:
            contagem = contagem + 1
    if contagem <= 2:
        return True
    else:
        return False