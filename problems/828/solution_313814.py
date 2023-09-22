def primo(n):
   	'''Função que verifica se o numero é primo ou não;
    int-> bool'''
    count = 1
    #if n < 0:
    #    return "Error"
    for i in range(1, int(n//2+1)):
        if n % i == 0:
            count=count+1

    if count > 2:
        return False
    else:
        return True