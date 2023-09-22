def primo(n):
    """funcao calcula e retorna se um dado numero n fornecido e primo ou nao

       int-> booleano
    """
    
    divisores=[]
    
    for i in range (1 , n+1):
        if n%1==0:
            list.append(divisores,i)
            
    if len(divisores) == 2:
        return "True"
    else:
        return "False"