def primo (numeroPos):
    '''Dado um número inteiro positivo, verifique se ele 
       é primo ou não e retorne um valor booleano;
       int -> bool'''
    cont = 0
    if (numeroPos%2)==0:
        return False
    for i in list(range(1, numeroPos+1, 2)):
        if (numeroPos%i)==0:
            cont = cont+1
    if cont==2:
        return True
    else:
        return False