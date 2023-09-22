def qtd_divisores(n):
    """ funcao que recebe um numero(n) como entrada, calcula os 
    numeros divisiveis por n e retorna a 
    quantidade de divisores.
    entrada->int
    saida->int
    """
    div=[]
    
    for i in range(1,n+1):
        if n%i==0:
            div= div+[i]
        
    return len(div)