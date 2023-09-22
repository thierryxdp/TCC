def primo(numero):
    ''' Entrada: numero -> dado do tipo inteiro
    	
        Saída: retorna um valor booleano indicando se o número é
        	  primo ou não
              
        int -> bool'''
    if qtd_divisores(numero) == 2:
        return True
    else:
        return False