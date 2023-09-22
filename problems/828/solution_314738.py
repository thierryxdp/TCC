def primo(numero):
    """Dado um número como parâmetro, a função vai
    verificar se este número é primo ou não. A função
    retorna True se ele for e False se não for.
    int --> bool"""
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