def fatorial (num):
    """Função que irá calcular o fatorial de um número , float->int->float"""
    fator=1
    while num>0:
        fator= num*fator
        num= num-1
    return fator