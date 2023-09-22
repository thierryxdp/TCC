def primo(numero):
    """ Função que dado um número inteiro posistivo, verifique se este número é primo ou não
    int -> bool"""
    
    for num in range(2,numero//2+1):
        if numero % num == 0:
            return False
        
    else:
        return True