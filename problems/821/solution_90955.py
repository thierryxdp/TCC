def fatorial (numero):
    '''Função que retornao fatorial de número. int - > int'''
    resultado=1
    cont=1
    while cont <= numero:
        resultado =resultado * cont
        cont = cont + 1
    return resultado