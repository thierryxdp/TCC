def primo(numero):
    divisores = 0
    lista = range(1,(numero+1))
    for num in lista:
         if numero%num==0:
            divisores = divisores + 1
    if divisores == 2:
        return True
    if divisores == 1:
        return True
    else:
        return False