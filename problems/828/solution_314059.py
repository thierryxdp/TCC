def primo(n):
    """
    Função que dado um inteiro positivo retorna um valor
    booleano se for primo.(True se sim. False se não.)
    """
    qtd_divisores=0
    lista_divisores=list(range(1,n+1))
    
    for i in lista_divisores[0:n+1:(n//2)+1]:
        if n%i==0:
            qtd_divisores+=1
        
        else:
            if n%i==0:
                qtd_divisores+=1  
    if qtd_divisores==2:
        return True
    else:
        return False