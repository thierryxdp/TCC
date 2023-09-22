def qtd_divisores(numero):
    '''funçao que conta quantos divisores um numero tem;
    int -> int'''
    lista = []
    for i in range(numero):
        if numero%(i+1)==0:
            lista += [(i+1),]
    return len(lista)