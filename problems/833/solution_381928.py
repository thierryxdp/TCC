def conta_numero(n,matriz):
    '''Função conta quantas vezes um dado número está em uma matriz;
    int,list -> int'''
    conta = 0

    for i in matriz:
        
        conta += i.count(n)

    return conta