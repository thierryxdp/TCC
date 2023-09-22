def primo(n):
    """Dada um número n, a função verifica se ele é primo
    ou não, retornando True se for e False caso não seja.
    Parametros de Entrada: int
    Retorna: bool"""
    
    contador=0
    
    if (n%2)==0:
        return False

    for i in list(range(1,n+1,2)):
        if (n%i)==0:
            contador=contador+1
    
    if contador==2:
        return True
    else:
        return False