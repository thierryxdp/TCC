def primo(n):
    
    '''Função que dado um número inteiro positivo como entrada, retorna se esse número é primo ou não. int -> bool'''
   
    for i in range(3,n,2):
        if n%i == 0 or n%2 == 0:
            return False
        else:
            return True