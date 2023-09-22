def qtd_divisores(x):
    """
    recebe um número e retorna a quantidade de divisores do mesmo
    """
    
    div=[]
    for i in range(x):
        if  x%i+1==0:
            list.append(div,i)
            
    return len(div)