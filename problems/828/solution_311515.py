def primo(n):
    '''Função verifica se um dado número n é primo;
    int -> bool'''
    for i in range(2,n+1):
        if i != n:
            i = n%i
            if i == 0:
                return False
        else:
        	return True