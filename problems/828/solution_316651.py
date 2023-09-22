def primo(numero):
    ''' Verifica se o dado número é primo
    int -> bool'''
    
    qtd_divisores = 0
    for i in range(2, numero+1):
        if numero%i == 0:
            qtd_divisores += 1
            
	if qtd_divisores == 1:
        return True
    return False