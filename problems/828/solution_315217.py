def primo(n):
    """ função que recebe um número inteiro e positivo e retorna
    uma expressão boleana se o número for primo ou não
    int->bool"""
    divisores=0
    for i in range(int(n/2)):
        if n%(2+i)!=0:
            divisores=True
        if n%(i+2)==0:
             return False
    return divisores