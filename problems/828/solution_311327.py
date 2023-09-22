def primo(inteiro):
    """Dado um numero inteiro positivo,retorna true ou false para sua primalidade.int-->bool"""
    i=inteiro
    divisores=0
    while i>0:
        if inteiro%i==0:
            divisores=divisores+1
    i=i-1
    if divisores==2:
        return True
    if divisores!=2:
        return False