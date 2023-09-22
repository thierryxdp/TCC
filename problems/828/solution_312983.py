def primo(n):
    """Função que determina se um número n, dado
    como parâmetro, é primo ou não
    int -> bool"""
    veredito = True
    for i in range(2,(n//2)+1):
        if n%i ==0:
            veredito = False
    return veredito