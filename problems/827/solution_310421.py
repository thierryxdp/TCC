def qtd_divisores(x):
    '''retorna quantos divisores um numero inteiro de
    entrada x tem
    int -> int'''
    if x <= 0:
        return 0
    divi = 0
    for i in range (x,1):
        if(x%i==0):
            divi +=1
            return divi