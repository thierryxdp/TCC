def primo(num):
    """Cálculo de uma função que recebe um número inteiro positivo como entrada 
    e verifica se este é primo ou não. 
    
        Parameters:
        num: número inteiro positivo a ser verificado 
        
        Returns:
        Retorna se o número dado como entrada é primo, dado que:
        int -> bool"""
    lista=0
    for p in range(2,num):
        if num%p==0 and p>=2:
            lista=lista+1
    if lista>=1:
        return False
    else:
        return True