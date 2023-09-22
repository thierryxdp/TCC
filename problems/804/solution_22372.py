def filtra_pares(elemento0,elemento1,elemento2,elemento3)
    '''Função que retorna os elementos pares de uma tupla de quatro elementos, em ordem;
    entrada: int, int, int, int;
    saída: tuple;
    '''
    if ((elemento0%2)==0):
        sopares=(elemento0,) #caso em que o elemento 0 somente é par;
    elif ((elemento1%2)==0):
        sopares=(elemento1,) #caso em que o elemento 1 somente é par;
    elif ((elemento2%2)==0):
        sopares=(elemento2,) #caso em que o elemento 2 somente é par;
    elif ((elemento3%2)==0):
        sopares=(elemento3,) #caso em que o elemento 3 somente é par;
    elif (((elemento0%2)==0) and ((elemento1%2)==0)):
        sopares=(elemento0,elemento1) #caso em que os elementos 0 e 1 são pares;
    elif (((elemento0%2)==0) and ((elemento2%2)==0)):
        sopares=(elemento0,elemento2) #caso em que os elementos 0 e 2 são pares;
    elif (((elemento0%2)==0) and ((elemento3%2)==0)):
        sopares=(elemento0,elemento3) #caso em que os elementos 0 e 3 são pares;
    elif (((elemento1%2)==0) and ((elemento2%2)==0)):
        sopares=(elemento1,elemento2) #caso em que os elementos 1 e 2 são pares;
    elif (((elemento1%2)==0) and ((elemento3%2)==0)):
        sopares=(elemento1,elemento3) #caso em que os elementos 1 e 3 são pares;
    elif (((elemento2%2)==0) and ((elemento3%2)==0)):
        sopares=(elemento2,elemento3) #caso em que os elementos 2 e 3 são pares;
    elif (((elemento0%2)==0) and ((elemento1%2)==0) and ((elemento2%2)==0)):
        sopares=(elemento0,elemento1,elemento2) #caso em que os elementos 0, 1 e 2 são pares;
    elif (((elemento0%2)==0) and ((elemento1%2)==0) and ((elemento3%2)==0)):
        sopares=(elemento0,elemento1,elemento3) #caso em que os elementos 0, 1 e 3 são pares;
    elif (((elemento0%2)==0) and ((elemento2%2)==0) and ((elemento3%2)==0)):
        sopares=(elemento0,elemento2,elemento3) #caso em que os elementos 0, 2 e 3 são pares;
    elif (((elemento1%2)==0) and ((elemento2%2)==0) and ((elemento3%2)==0)):
        sopares=(elemento1,elemento2,elemento3) #caso em que os elementos 1, 2 e 3 são pares;
    elif (((elemento0%2)==0) and ((elemento1%2)==0) and ((elemento2%2)==0) and ((elemento3%2)==0)):
        sopares=(elemento0,elemento1,elemento2,elemento3) #caso em que todos os elementos são pares;
    else:
        sopares=()
    return sopares