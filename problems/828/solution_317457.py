def primo(numero):
    ''' função que dado um número verifica se este numero é primo ou não.
        int ---> int '''
    quantidade_de_divisores = []
    a = numero
    for numero in range(1,a+1):
        if a % numero == 0:
            list.append(quantidade_de_divisores, numero)
            numero -= 1
        else:
            numero -=1
    if len(quantidade_de_divisores) > 2:
        return False
    else:
        return True
    
##Não consegui utilizar a dica 2, porém são 2:47 da manhã, amanhã ou na próxima aula eu tento fazer novamente.