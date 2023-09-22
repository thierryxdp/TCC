def primo(n):
    """"função que dado um número inteiro positivo, verifica se este é primo ou não, retornando um valor bool.
    
    int -> bool
    
    exemplos:
    primo(1)===False
    primo(0)==False
    primo(17)==True"""
    resultado=0
    for i in range(1,n+1):
        if n%i==0:
            resultado=resultado+1
    if resultado > 2:
        return False
    if resultado==2:
        return True
    if resultado<2:
        return False