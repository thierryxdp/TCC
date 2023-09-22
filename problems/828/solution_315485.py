def primo(n):
    """
    Função recebe um numero inteiro positivo n, e retorna True caso n seja um número
    primo e False caso não seja.
    int -> booleano
    """
    divisores=0
    for i in range(1,n+1):
        if (n%i)==0:
            divisores+=1  
    return divisores==2