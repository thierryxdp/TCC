def primo(num):
    """Cálculo de uma função que recebe um número inteiro positivo como entrada 
    e verifica se este é primo ou não. 
    
        Parameters:
        num: número inteiro positivo a ser verificado 
        
        Returns:
        Retorna se o número dado como entrada é primo, dado que:
        int -> bool"""
    primo=0
    for p in range(0,num+1):
        if num%p==0:
            return True
        else:
            return False