def soma_h(num):
    '''Função que calcula e retorna o alor H com N termos
    onde N é inteiro e dado com entrada.
    num=int->float'''
    w=range(1,num+1)
    s=0
    for y in w:
        s=s+(1/y)
    return round(s,2)